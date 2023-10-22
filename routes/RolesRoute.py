from typing import Optional
from flask import Blueprint, request, jsonify
from services.RolesService import RolesService
from schemas.RolesSchemas import CreateRoleSchema, UpdateRoleSchema
from auth.JwtUtils import validate_token

rolesService: RolesService = RolesService()
bp = Blueprint('roles', __name__, url_prefix='/roles')

@bp.before_request
def before_request():
    token = request.args.get("Authorization").split(" ")[1]
    response = validate_token(token, output=True)
    if response['roleId'] != 10:
        raise Exception("Unauthorized")

@bp.route("/", methods=['GET'])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0
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

    data = [
        calzado.__repr__()
        for calzado in rolesService.list(
            name, pageSize, startIndex
        )
    ]

    return {
        "status": data is not None,
        "data": data,
        "total": len(data)
    }

@bp.route("/<int:roleId>", methods=['GET'])
def get(
    roleId: int
):
    response = rolesService.get(roleId)

    return {
        "status": response is not None,
        "data": response.__repr__()
    }

@bp.route("/", methods=['POST'])
def create():
    json_input = request.get_json()
    schema = CreateRoleSchema()
    obj = schema.load(json_input)
    result = rolesService.create(obj)
    return {
        "status": result is not None,
        "data": result.__repr__()
    }

@bp.route("/", methods=['PUT'])
def update():
    json_input = request.get_json()
    schema = UpdateRoleSchema()
    role_body = schema.load(json_input)
    result = rolesService.update(role_body)
    return jsonify({
        "status": result is not None,
        "data": result.__repr__()
    })

@bp.route("/<int:roleId>", methods=['DELETE'])
def delete(
    roleId: int,
):
    result = rolesService.delete(roleId)
    return jsonify({
        "status": result is not None,
        "message": "Role deleted"
    })
    

