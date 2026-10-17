from flask import Flask, abort, jsonify, request
from data import products

app = Flask(__name__)

# TODO: Implement homepage route that returns a welcome message
@app.route("/")
def home():
  return jsonify(message="Welcome to the Products API!")


# TODO: Implement GET /products route that returns all products or filters by category if provided
@app.route("/products")
def get_products():
  category = request.args.get("category")
  if category:
    filtered = [p for p in products if p["category"].lower() == category.lower()]
    return jsonify(filtered)
  return jsonify(products)


# TODO: Implement GET /products/<id> route that returns a specific product by ID or 404 if not found
@app.route("/products/<int:id>")
def get_product_by_id(id):
  product = next((p for p in products if p["id"] == id), None)
  if product is None:
    abort(404, description="Product not found")
  return jsonify(product)


if __name__ == "__main__":
  app.run(debug=True)