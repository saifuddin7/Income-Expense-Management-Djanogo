from django.shortcuts import render,redirect,HttpResponse
from .models import UserInfoForm,UserInfo
from django.contrib.auth.models import User
from expense.models import Expense
from income.models import Income

#calculating balance amt based on income and expense
def get_balance(request):
    uid=request.session.get('uid')  #getting the session id
    incl=Income.objects.filter(user=uid) #getting values based on session id
    total_income=0 
    for i in incl: #iterating on all fields of user
        total_income+=i.income #adding income of user in total_income

    expl=Expense.objects.filter(user=uid)
    total_expense=0
    for i in expl:
        total_expense+=i.expense

    return total_income-total_expense


def home(request):
    bal=get_balance(request) #getting get_balance() to display on home.html
    context={'bal':bal} #saving in dict() format as usual
    return render(request,'home.html',context) 

def register(request):
    if request.method=='POST':
        f=UserInfoForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserInfoForm
        context={'form':f}
        return render(request,'register.html',context)

def acclist(request):
    uid=request.session.get('uid')
    l=UserInfo.objects.filter(id=uid)
    context={'l':l}
    return render(request,'acclist.html',context)


#login and logout functiones
from django.contrib.auth import login,logout,authenticate

def login_view(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            context={'msg':'Invalid Username and password'}
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

#edit profile function
def update_user(request):
    uid=request.session.get('uid')
    u=UserInfo.objects.get(id=uid)
    if request.method=='POST':
        f=UserInfoForm(request.POST,instance=u)
        f.save()
        return redirect('/')
    else: 
        f=UserInfoForm(instance=u)
        context={'form':f}
        return render(request,'register.html',context)