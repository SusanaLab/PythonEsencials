from flask import Flask
from flask_restful import Resource, Api
from routes import RutasApi

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.mmdjfqqxibtlmbrezcly:4waxpsEchVKiKwkp@aws-1-us-east-2.pooler.supabase.com:6543/postgres'

api = Api(app)

routes = RutasApi()
routes.inicializar_rutas(api)

app.run(debug=True, port=8000)
