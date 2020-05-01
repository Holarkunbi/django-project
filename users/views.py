from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
# Create your views here.
def home(request):
    template = 'users/index.html'
    context = {

    }
    return render(request, template, context)

def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

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
        print(user)

        if user is not None:
            if user.is_active:
               login(request, user)
               print("Login success")
               return HttpResponseRedirect(reverse('home'))
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
    return HttpResponseRedirect(reverse('home'))