from flask import jsonify, send_file
from flask import request
from src.util.authorization import auth_required
from init import app, IMAGE_ROOT
from src.data.model import Article, ArticleSchema, Author
from src.data import dboperator
from src.data.dboperator import DatabaseError
from src.util.funcs import crop_image1x1, crop_image2x1, crop_image4x3, crop_image16x9


# Service layer


@app.route( '/<int:pid>', methods=['GET'] )
@auth_required
def index(pid):
    row = dboperator.getrow( Article, pid )
    if row is not None:
        article_schema = ArticleSchema()
        return jsonify( article_schema.dump( row ).data )
    else:
        return jsonify( {'Error': "Record not found"} )


@app.route( '/create_author', methods=['POST'] )
@auth_required
def create_author():
    try:
        data = request.get_json()
        new_author = Author( name=data['name'] )
        rtn = dboperator.insert( new_author )
    except KeyError:
        return jsonify( {'Error': "Json key error"} )
    except DatabaseError as e:
        return jsonify( {'Error': "database error",
                         'Description': str( e )} )
    return jsonify( {'Inserted id ': rtn} )


@app.route( '/create', methods=['POST'] )
@auth_required
def create():
    try:
        data = request.get_json()
        new_article = Article( title=data['title']
                               , body=data['body']
                               , site=data['site']
                               , author_id=data['author'] )
        rtn = dboperator.insert( new_article )
    except KeyError:
        return jsonify( {'Error': "Json key error"} )
    except DatabaseError as e:
        return jsonify( {'Error': "database error",
                         'Description': str( e )} )
    return jsonify( {'Inserted id ': rtn} )


@app.route( '/update/<int:pid>', methods=['PUT'] )
@auth_required
def update(pid):
    try:
        data = request.get_json()
        upd_article = dboperator.getrow( Article, pid )
        if upd_article is not None:
            upd_article.title = data['title']
            upd_article.body = data['body']
            upd_article.site = data['site']
            upd_article.author_id = data['author']
            upd_article.isupdate = 1
            dboperator.update()
        else:
            return jsonify( {'Error': "Record not found"} )
    except KeyError:
        return jsonify( {'Error': "Json key error"} )
    except TypeError:
        return jsonify( {'Error': "Json type error"} )
    except DatabaseError as e:
        return jsonify( {'Error': "database error",
                         'Description': str( e )} )
    return jsonify( {'Updated id ': pid} )


@app.route( '/delete/<int:pid>', methods=['POST'] )
@auth_required
def delete(pid):
    try:
        del_result = dboperator.delete( Article, pid )
    except DatabaseError as e:
        return jsonify( {'Error': "database error",
                         'Description': str( e )} )
    return jsonify( {'Deleted id ': del_result} if del_result > 0 else {'Error': "Record not found"} )


@app.route( '/upload/<int:pid>', methods=['POST'] )
def upload(pid):
    try:
        file = request.files['image']
        article = dboperator.getrow( Article, pid )
        if article is not None:
            destination = "\\".join( [IMAGE_ROOT, str( article.id ) + '.jpg'] )
            print( destination )
            file.save( destination )
        else:
            return jsonify( {'Error': "Record not found"} )
    except (FileExistsError, FileNotFoundError) as e:
        return jsonify( {'Error': "file error",
                         'Description': str( e )} )
    return jsonify( {'upload id ': pid} )


@app.route( '/download/<int:pid>', methods=['GET'] )
def download(pid):
    try:
        article = dboperator.getrow( Article, pid )
        if article is not None:
            source = "\\".join( [IMAGE_ROOT, str( article.id ) + '.jpg'] )
            return send_file( source, mimetype='image/jpeg' )  # response
        else:
            return jsonify( {'Error': "Record not found"} )
    except DatabaseError as e:
        return jsonify( {'Error': "database error",
                         'Description': str( e )} )


# 1x1, 2x1, 4x3, 16x9

@app.route( '/download/<int:pid>/<crop>', methods=['GET'] )
def download_crop(pid, crop):
    try:
        article = dboperator.getrow( Article, pid )
        if article is not None:
            source = "\\".join( [IMAGE_ROOT, str( article.id ) + '.jpg'] )
            cropfile = "\\".join( [IMAGE_ROOT, str( article.id ) + '_' + crop + '.jpg'] )
            if crop == '1x1':
                crop_image1x1( source, cropfile )
            elif crop == '2x1':
                crop_image2x1( source, cropfile )
            elif crop == '4x3':
                crop_image4x3( source, cropfile )
            elif crop == '16x9':
                crop_image16x9( source, cropfile )

            return send_file( cropfile, mimetype='image/jpeg' )  # response
        else:
            return jsonify( {'Error': "Record not found"} )
    except DatabaseError as e:
        return jsonify( {'Error': "database error",
                         'Description': str( e )} )


if __name__ == "__main__":
    print( {'Image Root': IMAGE_ROOT} )
    app.run( debug=True )
