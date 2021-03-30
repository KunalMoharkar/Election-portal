from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from Election.models import Election

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"accounts/login.html",{"message":None})
    context = {
        "user": request.user ,
        "elections": Election.objects.all()
    }
    return render(request,"accounts/dashboard.html",context)

def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request,username = username,password = password)
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"accounts/login.html",{"message":"Invalid Credentials!!"})

def logout_view(request):
    logout(request)
    return render(request,"accounts/login.html",{"message":"Logged out successfully"})