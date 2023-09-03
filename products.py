from flask import Flask, jsonify, request
import json
from flask_cors import CORS
from werkzeug.exceptions import HTTPException
#from flask_swagger import swagger


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

app = Flask("Product server")

@app.route("/products", methods = ['GET'])
def get_products():
    return jsonify(products)

@app.route("/products/<id>", methods = ['GET'])
def get_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    return jsonify(product)

@app.route("/products", methods = ['POST'])
def add_products():
    products.append(request.get_json())
    return '', 201

@app.route("/products/<id>", methods = ['PUT'])
def update_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    updated_product = request.get_json()
    for key, value in updated_product.items():
        product[key] = value
    return '', 204

@app.route("/products/<id>", methods = ['DELETE'])
def delete_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '', 204

# @app.route('/swaggerfile')
# def send_swagger():
#   return send_from_directory('.', "swagger_config.json")

# @app.route("/spec")
# def spec():
#     swag = swagger(app)
#     swag['info']['title'] = "Cat stationery"
#     swag['info']['version'] = '1.0.0'
#     swag['info']['description'] = "Cat themed overpriced stationery"
#     return jsonify(swag)

@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code" : e.code,
        "name" : e.name,
        "description" : e.description
    })
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    CORS(app)
    
