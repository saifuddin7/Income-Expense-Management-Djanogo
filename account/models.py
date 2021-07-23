from django.db import models

from django.contrib.auth.models import User

class UserInfo(User):
    age=models.IntegerField()
    contact=models.CharField(max_length=30)
    address=models.TextField(max_length=300)

from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserInfoForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name','age','email','contact','address','password1','password2']
