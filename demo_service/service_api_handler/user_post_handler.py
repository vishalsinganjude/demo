from datetime import datetime
from demo_service.db.user_model.models import User

def create_user(req_data):
    username = req_data['u_name']
    first_name = req_data['firstName']
    last_name = req_data['lastName']
    email_id = req_data['email_id']
    phone = req_data['phone']
    password = req_data['password']
    DOB = req_data['DOB']
    gender = req_data['gender']
    profile_pic = req_data['profile_pic']
    try:
        user_object = User.objects.create(username = username,
                                          first_name = first_name,
                                          last_name = last_name,
                                          phone = phone,
                                          DOB = DOB,
                                          password = password,
                                          gender = gender,
                                          profile_pic = profile_pic)
        return user_object
    except:
        return None
