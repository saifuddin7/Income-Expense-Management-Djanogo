from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import IncForm,Income


def incform(request):
    if request.method=='POST':
        i=Income()
        uid=request.session.get('uid')
        i.income=request.POST.get('income')
        i.incomeType=request.POST.get('incomeType')
        i.description=request.POST.get('description')
        i.user=User.objects.get(id=uid)
        i.save()
        return redirect('/')
    else:
        f=IncForm
        context={'form':f}
        return render(request,'incform.html',context)


#displaying the sorting bar and search by dicription
def income_list(request):
    uid=request.session.get('uid')
    incl=Income.objects.filter(user=uid)
    inc=set()
    inctype=set()
    for i in incl:
        inc.add(i.income)
        inctype.add(i.incomeType)
        
    #sorting by disription
    if request.method=='POST':
        search=request.POST.get('search')
        incl=Income.objects.filter(user=uid,description__contains=search)
        context={'incl':incl,'inc':inc,'inctype':inctype}
        return render(request, 'income_list.html',context)
    #displaying all income of session user
    else:    
        context={'incl':incl,'inc':inc,'inctype':inctype}
        return render(request, 'income_list.html',context)


#sorting with income,incomeType,incomeDate
def sortby_income(request,inc):
    uid=request.session.get('uid')
    incl=Income.objects.filter(user=uid,income=inc)
    inc=set()
    inctype=set()
    
    for i in Income.objects.filter(user=uid):
        inc.add(i.income)
        inctype.add(i.incomeType)
        
    
    context={'incl':incl,'inc':inc,'inctype':inctype}
    return render(request, 'income_list.html',context)

def sortby_incometype(request,inctype):
    uid=request.session.get('uid')
    incl=Income.objects.filter(user=uid,incomeType=inctype)
    inc=set()
    inctype=set()
    
    for i in Income.objects.filter(user=uid):
        inc.add(i.income)
        inctype.add(i.incomeType)
        
    
    context={'incl':incl,'inc':inc,'inctype':inctype}
    return render(request, 'income_list.html',context)


#delete and edit function
def delete_inc(request):
    iid=request.GET.get('id')
    inc=Income.objects.get(id=iid)
    inc.delete()
    return redirect('/income-list')

def edit_inc(request):
    iid=request.GET.get('id')
    inc=Income.objects.get(id=iid)
    if request.method=='POST':
        incf=IncForm(request.POST,instance=inc)
        incf.save()
        return redirect('/income-list')
    else:
        incf=IncForm(instance=inc)
        context={'form':incf}
        return render(request,'incform.html',context)

