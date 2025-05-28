from django.shortcuts import render
from .models import Users


def GetAllUsers():
    users = Users.objects.all()
    
# Create your views here.
