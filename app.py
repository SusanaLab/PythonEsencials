from flask import Flask
from flask_restful import Resource, Api
from routes import RutasApi

app = Flask(__name__)
api = Api(app)

routes = RutasApi()
routes.inicializar_rutas(api)

app.run(debug=True, port=8000)
