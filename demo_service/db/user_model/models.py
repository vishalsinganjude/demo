import uuid
from datetime import datetime

from django.db import models

class User(models.Model):
    Genders =(("MALE", "MALE"),
              ("FEMALE", "FEMALE"),
              ("OTHER", "OTHER"))
    u_name = models.CharField(max_length=200,primary_key=True)
    firstName = models.CharField(max_length=200,null=True)
    lastName = models.CharField(max_length=200, null=True)
    email_id = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,null=True)
    DOB = models.DateTimeField(null=True)
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=200,choices=Genders, default= None)
    profile_pic = models.CharField(max_length=500)
    created_on = models.DateTimeField(default=datetime.now())
