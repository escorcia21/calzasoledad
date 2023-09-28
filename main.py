from flask import Flask
from routes.Api import bp as main_bp
from routes.Calzado import bp as calzado_bp
from models.BaseModel import init
from http.client import HTTPException
from flask import jsonify

app = Flask(__name__)

# Register blueprints here
main_bp.register_blueprint(calzado_bp)
app.register_blueprint(main_bp)

# Initialize database
init()

@app.route("/test")
def hello_world():
    return "Hello, World!"

@app.errorhandler(Exception)
def handle_error(e):
    code = 500

    if isinstance(e, HTTPException):
        code = e.code
        
    return jsonify(error=str(e)), code