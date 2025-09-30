from flask_restful import Resource
from flask import render_template, make_response, request


class HelloWorld(Resource):
    def get(self):
        return "Hola mundo"


class InicioDeSesion(Resource):
    def get(self):
        return make_response(render_template("login.html"))

    def post(self):
        print("---LLA INFORMACION SE ESTA PROCESANDO")
        correo = request.form.get("email")
        password = request.form.get("password")

        if correo == "susanlevart@gmail.com":
            print("el correo es correcto")

        print(f"Correo:{correo}")
        print(f"Password:{password}")

        return "procesando incion de sesion.."


# 4waxpsEchVKiKwkp
class RegistroDeUsuario(Resource):
    def get(self):
        return make_response(render_template("registro.html"))

    def post(self):
        print("Processando")

        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        password = request.form.get("password")
        telefono = request.form.get("telefono")

        return "Procesando registro de usuario"
