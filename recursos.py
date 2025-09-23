from flask_restful import Resource
from flask import render_template, make_response


class HelloWorld(Resource):
    def get(self):
        return 'Hola mundo'
    

class InicioDeSesion(Resource):
    def get(self):
        return make_response(render_template("login.html"))


class RegistroDeUsuario(Resource):
    def get(self):
        return make_response(render_template("registro.html"))

