from typing import Optional
from flask import Blueprint, request
from services.RolesService import RolesService
from schemas.RolesSchemas import CreateRoleSchema


bp = Blueprint('roles', __name__, url_prefix='/roles')

@bp.route("/", methods=['GET'])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    calzadoService: RolesService = RolesService()
):

    return [
        calzado
        for calzado in calzadoService.list(
            name, pageSize, startIndex
        )
    ]

@bp.route("/<int:roleId>", methods=['GET'])
def get(
    roleId: int,
    calzadoService: RolesService = RolesService()
):
    return calzadoService.get(roleId)

@bp.route("/", methods=['POST'])
def create(
    calzadoService: RolesService = RolesService()
):
    data = request.json
    schema = CreateRoleSchema()
    role, errors = schema.load(data)
    if errors:
        print(errors)
    else:
        return calzadoService.create(role)

