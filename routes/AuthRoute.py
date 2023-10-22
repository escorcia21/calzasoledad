from flask import Blueprint, request, jsonify
from services.UsersService import UsersService
from schemas.UsersSchemas import LoginUserSchema
from auth.JwtUtils import write_token, validate_token

bp = Blueprint("auth", __name__, url_prefix="/auth")

usersService = UsersService()

@bp.route("/", methods=["POST"])
def login():
    json_input = request.get_json()

    schema = LoginUserSchema()
    obj = schema.load(json_input)

    user = usersService.login(obj)

    if user:
        token = write_token({"cc": user.cc, "roleId": user.roleId})
        print(token)
        return {"token": token}
    else:
        return {"message": "Invalid credentials"}, 401
    
@bp.route("/verify", methods=["POST"])
def verify():
    token = request.headers.get("Authorization").split(" ")[1]
    return validate_token(token, output=True)

