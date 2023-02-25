from django.shortcuts import render
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from . import models
from datetime import date
from django.contrib.auth.decorators import login_required

# < Registration >

def customer_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        card = request.POST['card']
        country = request.POST['country']
        image = request.FILES['image']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "registration/customer_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        customer = customer.objects.create(user=user, card=card, country=country, image=image)
        user.save()
        customer.save()
        alert = True
        return render(request, "registration/customer_registration.html", {'alert':alert})
    return render(request, "registration/customer_registration.html")


def freelancer_registration(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        card = request.POST['card']
        country = request.POST['country']
        image = request.FILES['image']
        category = request.POST['category']
        name_job = request.POST['name_job']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "registration/freelancer_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,first_name=first_name, last_name=last_name)
        freelancer = freelancer.objects.create(user=user, card=card, country=country, image=image,name_job=name_job,category=category)
        user.save()
        customer.save()
        alert = True
        return render(request, "registration/freelancer_registration.html", {'alert':alert})
    return render(request, "registration/freelancer_registration.html")


def customer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a customer!!")
            else:
                return redirect("/index")
        else:
            alert = True
            return render(request, "registration/customer_login.html", {'alert':alert})
    return render(request, "registration/customer_login.html")


def freelancer_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a freelancer!!")
            else:
                return redirect("/index")
        else:
            alert = True
            return render(request, "registration/freelancer_login.html", {'alert':alert})
    return render(request, "registration/freelancer_login.html")

def change_password(request):
    if request.method == "POST":
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(current_password):
                u.set_password(new_password)
                u.save()
                alert = True
                return render(request, "registration/change_password.html", {'alert':alert})
            else:
                currpasswrong = True
                return render(request, "registration/change_password.html", {'currpasswrong':currpasswrong})
        except:
            pass
    return render(request, "registration/change_password.html")



def Logout(request):
    logout(request)
    return redirect ("/")


# < pages >


def index(request):

    category = category.objects.all()
    job = job.objects.order_by('-id')[:5]
    freelancer = freelancer.objects.order_by('-id')[:10]
    context = {"category":category, "job": job, "freelancer": freelancer}
# editing the name of models here!
    return render(request, "pages/index.html", context)


def job_details(request, pk):
    job = job.objects.get(pk=pk)
    customer = customer.objects.get(pk=pk)
    context = {"job": job, "customer": customer}
# removing the name user and replace it by customer
    if request.method =="POST":
         return redirect

    return render(request, "pages/job_details.html", context)





# def requestsadmin(request,pk):
#     customer = user.objects.get(pk=pk)
#     myjobs = jobs.objects.get(created_by = customer,freelancer=)

#     context = {"customer": customer, "myjobs": myjobs}
#     return render(request,"aa.html",context)
