from typing import Optional
from flask import Blueprint, request, jsonify
from services.ProductionService import ProductionService
from schemas.productionSchemas import CreateProductionSchema, UpdateProductionSchema, ProductionByUserSchema

bp = Blueprint("production", __name__, url_prefix="/production")
productionService = ProductionService()

@bp.route("/", methods=["GET"])
def list_production():
    employeeId = request.args.get("employeeId")
    pageSize = request.args.get("pageSize")
    startIndex = request.args.get("startIndex")
    date = request.args.get("date")

    return [
        production.__repr__()
        for production in productionService.list(employeeId, pageSize, startIndex, date)
    ]

@bp.route("/<int:employeeId>", methods=["GET"])
def get_production(employeeId: int):
    ProductionByUserSchema().load(request.args.to_dict())
    startProductionDate = request.args.get("startProductionDate")
    endProductionDate = request.args.get("endProductionDate")
    production = productionService.get(startProductionDate, endProductionDate, employeeId)
    return jsonify(production)

@bp.route("/", methods=["POST"])
def create_production():
    production_body = request.get_json()

    obj = CreateProductionSchema().load(production_body)

    production = productionService.create(obj)

    return jsonify({
        "message": "production created",
        "production": production.__repr__()
    })

@bp.route("/", methods=["PUT"])
def update_production():
    production_body = request.get_json()

    obj = UpdateProductionSchema().load(production_body)

    production = productionService.update(obj)

    return jsonify({
        "message": "production updated",
        "production": production.__repr__()
    })