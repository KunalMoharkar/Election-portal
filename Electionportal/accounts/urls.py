from django.urls import include
from django.contrib import admin
from django.urls import re_path, path
from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("",views.index, name='index'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("login",views.login_view, name='login'),
    path("logout",views.logout_view, name='logout')
]