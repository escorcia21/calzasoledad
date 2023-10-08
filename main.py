from flask import Flask
from marshmallow import ValidationError
from routes.Api import bp as main_bp
from routes.RolesRoute import bp as roles_bp
from models.BaseModel import init
from http.client import HTTPException
from flask import jsonify

app = Flask(__name__)

# Register blueprints here
main_bp.register_blueprint(roles_bp)
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