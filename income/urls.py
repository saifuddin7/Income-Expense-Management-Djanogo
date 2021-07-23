
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('-form',v.incform,name='inc'),
    path('-list',v.income_list,name='inclist'),

    path('-by-income/<int:inc>',v.sortby_income,name='sr_income'),
    path('-by-incometype/<str:inctype>',v.sortby_incometype,name='sr_incometype'),
    path('-all',v.income_list,name='all_income'),
   
   

    path('dinc',v.delete_inc),
    path('einc',v.edit_inc),
]
