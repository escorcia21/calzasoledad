from typing import Optional
from flask import Blueprint, request, jsonify
from services.RolesService import RolesService
from schemas.RolesSchemas import CreateRoleSchema, UpdateRoleSchema

rolesService: RolesService = RolesService()
bp = Blueprint('roles', __name__, url_prefix='/roles')

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

    return [
        calzado.__repr__()
        for calzado in rolesService.list(
            name, pageSize, startIndex
        )
    ]

@bp.route("/<int:roleId>", methods=['GET'])
def get(
    roleId: int
):
    response = rolesService.get(roleId)
    return jsonify(response.__repr__())

@bp.route("/", methods=['POST'])
def create():
    json_input = request.get_json()
    schema = CreateRoleSchema()
    obj = schema.load(json_input)
    result = rolesService.create(obj)
    return {
        "message": "Role created",
        "role": result.__repr__()
    }

@bp.route("/", methods=['PUT'])
def update():
    json_input = request.get_json()
    schema = UpdateRoleSchema()
    role_body = schema.load(json_input)
    result = rolesService.update(role_body)
    return jsonify({
        "message": "Role updated",
        "role": result.__repr__()
    })

@bp.route("/<int:roleId>", methods=['DELETE'])
def delete(
    roleId: int,
):
    rolesService.delete(roleId)
    return jsonify({
        "message": "Role deleted"
    })
    

