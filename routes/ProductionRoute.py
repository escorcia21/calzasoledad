from typing import Optional
from flask import Blueprint, request, jsonify
from services.ProductionService import ProductionService
from schemas.productionSchemas import CreateProductionSchema, UpdateProductionSchema, ProductionByUserSchema
from auth.JwtUtils import validate_token

bp = Blueprint("production", __name__, url_prefix="/production")

@bp.before_request
def before_request():
    token = request.args.get("Authorization").split(" ")[1]
    response = validate_token(token, output=True)
    valid_endpoints_for_employee = [
        "main.production.get_production",
    ]

    if response['roleId'] != 10:
        if request.endpoint not in valid_endpoints_for_employee:
            raise Exception("Unauthorized")
        
        if request.endpoint == "main.production.get_production":
            if response["cc"] != str(request.view_args["employeeId"]):
                raise Exception("Unauthorized")

productionService = ProductionService()

@bp.route("", methods=["GET"])
def list_production():

    data = productionService.list()

    return {
        "status": data is not None,
        "data": data,
        "total": len(data)
    }

@bp.route("<int:employeeId>", methods=["GET"])
def get_production(employeeId: int):
    ProductionByUserSchema().load(request.args.to_dict())
    startProductionDate = request.args.get("startProductionDate")
    endProductionDate = request.args.get("endProductionDate")
    production = productionService.get(startProductionDate, endProductionDate, employeeId)
    return jsonify(production)

@bp.route("", methods=["POST"])
def create_production():
    production_body = request.get_json()

    obj = CreateProductionSchema().load(production_body)

    production = productionService.create(obj)

    return jsonify({
        "status": production is not None,
        "data": production.__repr__()
    })

@bp.route("", methods=["PUT"])
def update_production():
    production_body = request.get_json()

    obj = UpdateProductionSchema().load(production_body)

    production = productionService.update(obj)

    return jsonify({
        "status": production is not None,
        "data": production.__repr__()
    })