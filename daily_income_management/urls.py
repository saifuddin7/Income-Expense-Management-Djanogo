
from django.contrib import admin
from django.urls import path,include
from account.views import home

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('acc',include(('account.urls','account'),namespace="accounts")),
    path('expense',include(('expense.urls','expense'),namespace='expenses')),
    path('income',include(('income.urls','income'),namespace='incomes')),

   

    path('',include('account.urls')),
    path('',include('income.urls')),
    path('',include('expense.urls')),

    
]
