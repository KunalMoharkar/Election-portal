from django.urls import include
from django.contrib import admin
from django.urls import re_path, path
from django.contrib.auth import authenticate, login
from .views import *

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login_view, name='login'),
    path('logout',views.logout_view, name='logout'),
    path('applyelection',views.apply_for_election, name='applyforElections'),
    path('profile_image_upload', views.profile_image_view, name = 'profile_image_upload'),
    path('candidateprofile/<int:candidate_id>', views.get_candidate_profile, name = 'candidate_profile'),
]