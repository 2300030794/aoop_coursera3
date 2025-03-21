from flask import Flask, jsonify, request
from service.models import db, Product

app = Flask(__name__)

@app.route("/products/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({"id": product.id, "name": product.name, "category": product.category, "available": product.available}), 200
    return jsonify({"error": "Product not found"}), 404
