from flask import Flask
from marshmallow import ValidationError
from routes.Api import bp as main_bp
from routes.RolesRoute import bp as roles_bp
from routes.UsersRoute import bp as users_bp
from routes.ProductsRoute import bp as products_bp
from routes.ProductionRoute import bp as production_bp
from routes.AuthRoute import bp as auth_bp
from models.BaseModel import init
from http.client import HTTPException
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Register blueprints here
main_bp.register_blueprint(roles_bp)
main_bp.register_blueprint(users_bp)
main_bp.register_blueprint(products_bp)
main_bp.register_blueprint(production_bp)
main_bp.register_blueprint(auth_bp)
app.register_blueprint(main_bp)

# Initialize database
init()

@app.route("/test")
def hello_world():
    return "Hello, World!"

@app.errorhandler(Exception)
def handle_error(e):

    if isinstance(e, HTTPException):
        code = e.code
    elif isinstance(e, ValidationError):
        code = 422
    else:
        code = 500
        
    return jsonify(error=str(e)), code