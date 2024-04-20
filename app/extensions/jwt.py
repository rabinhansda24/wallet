from flask import Flask
from flask_jwt_extended import JWTManager


jwt = JWTManager()

def initialize_jwt(app: Flask):
    global jwt
    jwt.init_app(app)
    return jwt