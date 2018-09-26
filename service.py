from flask import jsonify
from util.authorization import auth_required
from util.static import app
from data.datamodel import Product, ProductSchema


@app.route( '/' )
@auth_required
def index():
    first_product = Product.query.first()
    product_schema = ProductSchema()
    out = product_schema.dump( first_product ).data
    return jsonify( {'Product': out} )


if __name__ == "__main__":
    app.run( debug=True )
