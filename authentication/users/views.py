from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegistrationForm

# Create your views here.

def homeview(request):
    template = 'users/index.html'
    context = {

    }
    return render(request, template, context)

def registrationview(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your registration is successfull')
            messages.success(request, 'Proceed to login')
            return redirect("users:loginpage")
        else:
            messages.error(request, 'Unsuccessful registration')


    template = 'users/registration.html'
    context ={
        'form':form
    }
    return render(request, template, context)

def loginview(request):
    if request.method == 'POST':
        username =  request.POST.get('username')
        password =  request.POST.get('password')
        # print(username)
        # print(password)
        user = authenticate(username=username, password=password)
        # print(user)

        if user is not None:
            if user.is_active:
               login(request, user)
               print("Login success")
               return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("User is not active")
        else:
            print("Login failed, check username and password")
            return HttpResponse("Invalid login datail")
    else:
        template = 'users/loginpage.html'
        return render(request, template, {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))