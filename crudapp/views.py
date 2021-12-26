from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import employee
from .models import users

def index(request):
    a = True
    msg=""
    e = employee()
    all_in_users = users.objects.all()
    if request.method=="POST":
        e1=employee(request.POST)
        nm = request.POST.get('name')
        ph = request.POST.get('phone_no')

        if e1.is_valid():
            for i in range(len(users.objects.all())):
                if users.objects.all()[i].name == nm and users.objects.all()[i].phone_no == ph:
                    msg ="Employee already exist"
                    a=False
            
            if a:
                e1.save()
                msg="Employee data is added to database"
                
    return render(request,'crudapp/index.html',{'form':e,'all_users':all_in_users,'msg':msg})


def deletedata(request,id):
    del_id = users.objects.get(id=id)
    del_id.delete()
    return HttpResponseRedirect('/')


def updatedata(request,id):
    if request.method=="POST":
        obj = users.objects.get(id = id)
        # instance = obj here means that we want to change/update 'obj' that particular object of the class in database
        # whenever we want to make changes the object of the class in database we use instance = 'object to update'
        obj1 = employee(request.POST,instance=obj)
        if obj1.is_valid():
            obj1.save()

    # when method is get or when clicked on edit  
    obj3 = users.objects.get(id=id)
    obj2 = employee(instance=obj3)
    return render(request,'crudapp/index-2.html',{'form':obj2})