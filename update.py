from flask import Flask, jsonify, request
from service.models import db, Product

app = Flask(__name__)

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    if "name" in data:
        product.name = data["name"]
    if "category" in data:
        product.category = data["category"]
    if "available" in data:
        product.available = data["available"]

    db.session.commit()
    return jsonify({"id": product.id, "name": product.name, "category": product.category, "available": product.available}), 200
