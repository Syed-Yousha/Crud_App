import email
from unicodedata import name
from django.shortcuts import redirect, render
from . import models

# Create your views here.
def index(request):

    emp = models.employees.objects.all()

    context = {
        'emp':emp,
    }

    return render (request, 'index.html',context=context)


def add(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = models.employees(
            name = name,
            email = email,
            address = address,
            phone = phone
        )

        emp.save()
        return redirect('home')
    
    return render (request, 'index.html')


def edit(request):
    
    emp = models.employees.objects.all()

    context = {
        'emp' : emp,
    }

    return redirect(request, 'index.html', context = context)

def update(request,id):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = models.employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        )

        emp.save()
        return redirect('home')

    return redirect(request,'index.html')


def delete(request,id):

    emp = models.employees.objects.filter(id = id)
    emp.delete()
    
    context = {
        'emp': emp,
    }

    return redirect('home')