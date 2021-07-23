from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import ExpForm,Expense
from account.views import get_balance

def expform(request):
    if request.method=='POST':
        i=Expense()
        uid=request.session.get('uid')
        i.expense=request.POST.get('expense')
        i.expenseType=request.POST.get('expenseType')
        i.description=request.POST.get('description')
        i.user=User.objects.get(id=uid)
        
        bal=get_balance(request) #getting balance with get_balance()
        exp=request.POST.get('expense') #getting expense field for comparing
        if int(exp) < bal: #checking if entered amt in expense is less than available balance
            i.save()
            return redirect('/')
        else:
            ef=ExpForm
            context={'msg':"Your Expense Amount is Greater than Balance",'ef':ef}
            return render(request,'expform.html',context)
    else:
        ef=ExpForm
        context={'ef':ef}
        return render(request,'expform.html',context)

#displaying expense list of session user and searching based on discription
def exp_list(request):
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid)
    expense=set()
    exptype=set()
    for i in exp:
        expense.add(i.expense)
        exptype.add(i.expenseType)

    if request.method=='POST':
        search=request.POST.get('search')
        exp=Expense.objects.filter(user=uid,description__contains=search)
        context={'exp':exp,'expense':expense,'exptype':exptype}
        return render(request,'explist.html',context)
    else:
        exp=Expense.objects.filter(user=uid)
        context={'exp':exp,'expense':expense,'exptype':exptype}
        return render(request,'explist.html',context)

def sortby_expense(request,expense):
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid,expense=expense)
    expense=set()
    exptype=set()
    for i in Expense.objects.filter(user=uid):
        expense.add(i.expense)
        exptype.add(i.expenseType)

    context={'exp':exp,'expense':expense,'exptype':exptype}
    return render(request,'explist.html',context)

def sortby_expensetype(request,exptype):
    uid=request.session.get('uid')
    exp=Expense.objects.filter(user=uid,expenseType=exptype)
    expense=set()
    exptype=set()
    for i in Expense.objects.filter(user=uid):
        expense.add(i.expense)
        exptype.add(i.expenseType)

    context={'exp':exp,'expense':expense,'exptype':exptype}
    return render(request,'explist.html',context)


def delete_exp(request):
    eid=request.GET.get('id')
    exp=Expense.objects.get(id=eid)
    exp.delete()
    return redirect('/expense-list')

def edit_exp(request):
    eid=request.GET.get('id')
    exp=Expense.objects.get(id=eid)
    if request.method=='POST':
        ef=ExpForm(request.POST,instance=exp)

        bal=get_balance(request) #getting balance with get_balance()
        exp=request.POST.get('expense') #getting expense field for comparing
        if int(exp) < bal: #checking if entered amt in expense is less than available balance
            ef.save()
            return redirect('/')
        else:
            ef=ExpForm
            context={'msg':"Your Expense Amount is Greater than Balance",'ef':ef}
            return render(request,'expform.html',context)
    else:
        ef=ExpForm(instance=exp)
        context={'ef':ef}
        return render(request,'expform.html',context)


