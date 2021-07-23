
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('-register',v.register,name="reg"),
    path('-login',v.login_view,name="login"),
    path('-logout',v.logout_view,name="logout"),
    path('-update',v.update_user,name="editprof"),

    
]
