from typing import Optional
from flask import Blueprint, request, jsonify
from services.UsersService import UsersService
from schemas.UsersSchemas import CreateUserSchema, UpdateUserSchema

bp = Blueprint("users", __name__, url_prefix='/users')
usersService: UsersService = UsersService()

@bp.route("/", methods=["GET"])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
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
        user.__repr__()
        for user in usersService.list(
            name, pageSize, startIndex
        )
    ]

@bp.route("/<int:userId>", methods=["GET"])
def get(
    userId: int
):
    response = usersService.get(userId)
    return jsonify(response.__repr__())

@bp.route("/", methods=["POST"])
def create():
    json_input = request.get_json()
    schema = CreateUserSchema()
    obj = schema.load(json_input)
    result = usersService.create(obj)
    return {
        "message": "User created",
        "user": result.__repr__()
    }

@bp.route("/", methods=["PUT"])
def update():
    json_input = request.get_json()
    schema = UpdateUserSchema()
    user_body = schema.load(json_input)
    result = usersService.update(user_body)
    return jsonify({
        "message": "User updated",
        "user": result.__repr__()
    })

