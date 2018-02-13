from flask import Flask
import django
django.setup()

from flask_restful import Api

from demo_service.service_api.ping import Ping
from demo_service.service_api.user import UserHandler

app = Flask(__name__)

api = Api(app)

api.add_resource(Ping,'/ping')
api.add_resource(UserHandler, '/user', '/user/<string:username>')


if __name__ == "__main__":
    app.run(host = '0.0.0.1', port=2700,debug=True)