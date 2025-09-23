from recursos import *


class RutasApi:
    def inicializar_rutas(self, api):
        api.add_resource(HelloWorld, "/")
        api.add_resource(InicioDeSesion, "/login")
        api.add_resource(RegistroDeUsuario, "/signup")
