from flask import jsonify
from flask import request
from src.util.authorization import auth_required
from src.util.init import app
from src.data.model import Article, ArticleSchema
from src.data import dboperator
from src.data.dboperator import DatabaseError


@app.route( '/<int:pid>', methods=['GET'] )
@auth_required
def index(pid):
    row = dboperator.getrow( Article, pid )
    if row is not None:
        article_schema = ArticleSchema()
        return jsonify( article_schema.dump( row ).data )
    else:
        return jsonify( {'Error': "Record not found"} )


@app.route( '/insert', methods=['POST'] )
@auth_required
def insert():
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


@app.route( '/upload', methods=['POST'] )
def upload():
    file = request.files['inputFile']
    return file


if __name__ == "__main__":
    app.run( debug=True )
