from django.db import connections
from django.db.utils import OperationalError
from flask_restful import Resource



class Ping(Resource):
    def get(self):
        db_con = connections['default']
        try:
            cd = db_con.cursor()
        except OperationalError:
            return "failed to connect db !!!!!"
        else:
            return "Welcome to restful."