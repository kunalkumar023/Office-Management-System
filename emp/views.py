from datetime import datetime

from django.shortcuts import HttpResponse, redirect, render

from .models import employee

# Create your views here.

def home(request):
    return render(request,"home.html")

def viewemp(request):

    emp= employee.objects.all()

    context = {
        'emps' : emp
    }
    return render(request,"viewemp.html",context)

def addemp(request):

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        newemp = employee(firstname=fname, lastname=lname,salary=salary,bonus=bonus, hiredate=datetime.now())
        newemp.save()
        return HttpResponse('Employee added successfully')

    elif request.method == 'GET':
        return render(request,"addemp.html")

    else:
        return HttpResponse("Try again:")
def delemp(request):

    if request.method == 'POST':
        firstname = request.POST['name']
        
        employee.objects.get(firstname=firstname).delete()
        return HttpResponse("Employee removed successfully:")
        # Instance.del()

    return render(request,"delemp.html")

def filteremp(request):

    if request.method == 'POST':
        firstname = request.POST['name']

        emp = employee.objects.filter(firstname=firstname).values()
        context={
            'emps' : emp
        }
        return render(request,"filteremp1.html",context)
    elif request.method =='GET':
        return render(request,'filteremp.html')

    else:
        return HttpResponse("An error Error")

