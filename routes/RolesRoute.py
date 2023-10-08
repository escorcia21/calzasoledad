from typing import Optional
from flask import Blueprint, request, jsonify
from services.RolesService import RolesService
from schemas.RolesSchemas import CreateRoleSchema, UpdateRoleSchema


bp = Blueprint('roles', __name__, url_prefix='/roles')

@bp.route("/", methods=['GET'])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    calzadoService: RolesService = RolesService()
):
    reqName = request.args.get('name')
    if reqName:
        name = reqName
    
    reqPageSize = request.args.get('pageSize')
    if reqPageSize:
        pageSize = int(reqPageSize)

    reqStartIndex = request.args.get('startIndex')
    if reqStartIndex:
        startIndex = int(reqStartIndex)

    return [
        calzado.__repr__()
        for calzado in calzadoService.list(
            name, pageSize, startIndex
        )
    ]

@bp.route("/<int:roleId>", methods=['GET'])
def get(
    roleId: int,
    calzadoService: RolesService = RolesService()
):
    response = calzadoService.get(roleId)
    return jsonify(response.__repr__())

@bp.route("/", methods=['POST'])
def create(
    calzadoService: RolesService = RolesService()
):
    json_input = request.get_json()
    schema = CreateRoleSchema()
    obj = schema.load(json_input)
    result = calzadoService.create(obj)
    return {
        "message": "Role created",
        "role": result.__repr__()
    }

@bp.route("/", methods=['PUT'])
def update(
    calzadoService: RolesService = RolesService()
):
    json_input = request.get_json()
    schema = UpdateRoleSchema()
    role_body = schema.load(json_input)
    result = calzadoService.update(role_body)
    return jsonify({
        "message": "Role updated",
        "role": result.__repr__()
    })

@bp.route("/<int:roleId>", methods=['DELETE'])
def delete(
    roleId: int,
    calzadoService: RolesService = RolesService()
):
    calzadoService.delete(roleId)
    return jsonify({
        "message": "Role deleted"
    })
    

