from flask import jsonify
from flask import request
from util.authorization import auth_required
from util.static import app
from data.model import Article, ArticleSchema
from data import dboperator


@app.route( '/<int:pid>', methods=['GET'] )
@auth_required
def index(pid):
    first_product = Article.query.filter_by( id=pid ).first()
    product_schema = ArticleSchema()
    out = product_schema.dump( first_product ).data
    return jsonify( {'Article': out} )


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
    return jsonify( {'Inserted id ': rtn} )


@app.route( '/update', methods=['PUT'] )
@auth_required
def update():
    return "2"


@app.route( '/upload', methods=['POST'] )
def upload():
    file = request.files['inputFile']
    return file


if __name__ == "__main__":
    app.run( debug=True )
