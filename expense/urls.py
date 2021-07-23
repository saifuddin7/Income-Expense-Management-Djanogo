
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('-form',v.expform,name='exp'),
    path('-list',v.exp_list,name='explist'),

    path('-by-expense/<int:expense>',v.sortby_expense,name='sr_expense'),
    path('-by-expensetype/<str:exptype>',v.sortby_expensetype,name='sr_expensetype'),
    path('-all',v.exp_list,name='all_expense'),

    path('dexp',v.delete_exp),
    path('eexp',v.edit_exp),
]
