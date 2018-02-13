from flask import request
from flask_restful import Resource

from demo_service.service_api_handler import user_post_handler

class UserHandler(Resource):
    def post(self):
        request_data = request.get_json()
        result = user_post_handler.create_user(request_data)
        if result:
            return  {"success": "User succesfully created !!!"}
        else:
            return {"success": False}
    def get(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass