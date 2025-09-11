from flask import Flask
from flask_restful import Resource, Api

# estamos creando una instancia/objeto de flask
app = Flask(__name__)
# estamos creando una instancia/objeto de API(flask_restful)
api = Api(app)


# creamos un recurso
class HelloWorld(Resource):
    def get(self):

        return "hello world"


class InicioDeSesion(Resource):
    def get(self):

        return "Hola estamos construyendo un inicio de sesion"


# todo recurso que se cree va a estar representado por una clase
# todo recurso debe tener una ruta en especifico
api.add_resource(HelloWorld, "/")
api.add_resource(InicioDeSesion, "/login")

if __name__ == "__main__":
    app.run(debug=True, port=8000)
""" 192.168.0.112  """
