from typing import Optional
from flask import Blueprint, request, jsonify
from services.ProductsService import ProductsService
from schemas.ProductsSchemas import CreateProductSchema, UpdateProductSchema

bp = Blueprint("products", __name__, url_prefix="/products")
productsService = ProductsService()

@bp.route("/", methods=["GET"])
def list_products():
    name = request.args.get("name")
    pageSize = request.args.get("pageSize")
    startIndex = request.args.get("startIndex")

    data = [
        product.__repr__()
        for product in productsService.list(name, pageSize, startIndex)
    ]

    return {
        "status": data is not None,
        "data": data,
        "total": len(data)
    }

@bp.route("/<int:productId>", methods=["GET"])
def get_product(productId: int):
    product = productsService.get(productId)

    return {
        "status": product is not None,
        "data": product.__repr__()
    }

@bp.route("/", methods=["POST"])
def create_product():
    product_body = request.get_json()

    obj = CreateProductSchema().load(product_body)

    product = productsService.create(obj)

    return jsonify({
        "status": product is not None,
        "data": product.__repr__()
    })

@bp.route("/", methods=["PUT"])
def update_product():
    product_body = request.get_json()

    obj = UpdateProductSchema().load(product_body)

    product = productsService.update(obj)

    return jsonify({
        "status": product is not None,
        "data": product.__repr__()
    })
