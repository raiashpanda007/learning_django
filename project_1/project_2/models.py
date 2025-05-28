from django.db import models

class Users (models.Model):
    USER_TYPE =[
        ('AD','Admin'),
        ('US','User'),
    ]
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    type = models.CharField(max_length=2, choices=USER_TYPE )


# Create your models here.
