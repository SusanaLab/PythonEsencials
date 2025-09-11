# app/__init__.py
from flask import Flask
from flask_restful import Api
from .routes import APIRoutes

def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    routes = APIRoutes()
    routes.init_api(api)

    return app
  