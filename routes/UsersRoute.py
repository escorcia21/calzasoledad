from typing import Optional
from flask import Blueprint, request, jsonify
from services.UsersService import UsersService
from schemas.UsersSchemas import CreateUserSchema, UpdateUserSchema
from auth.JwtUtils import validate_token

bp = Blueprint("users", __name__, url_prefix='/users')
usersService: UsersService = UsersService()

@bp.before_request
def before_request():
    token = request.args.get("Authorization").split(" ")[1]
    response = validate_token(token, output=True)
    valid_endpoints_for_employee = [
        "main.users.get",
    ]
    
    if response['roleId'] != 10: 
        if request.endpoint not in valid_endpoints_for_employee:
            raise Exception("Unauthorized")
        if request.endpoint == "main.users.get":
            if response["cc"] != str(request.view_args["userId"]):
                raise Exception("Unauthorized")

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

    data = [
        user.__repr__()
        for user in usersService.list(
            name, pageSize, startIndex
        )
    ]

    return {
        "status": data is not None,
        "data": data,
        "total": len(data)
    }

@bp.route("/<int:userId>", methods=["GET"])
def get(
    userId: int
):
    response = usersService.get(userId)
    return {
        "status": response is not None,
        "data": response.__repr__()
    }

@bp.route("/", methods=["POST"])
def create():
    json_input = request.get_json()
    schema = CreateUserSchema()
    obj = schema.load(json_input)
    result = usersService.create(obj)
    return {
        "status": result is not None,
        "data": result.__repr__()
    }

@bp.route("/", methods=["PUT"])
def update():
    json_input = request.get_json()
    schema = UpdateUserSchema()
    user_body = schema.load(json_input)
    result = usersService.update(user_body)
    return jsonify({
        "status": result is not None,
        "data": result.__repr__()
    })

