from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import *

from Election.models import Election
from .models import Student, Candidate

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request,"accounts/login.html",{"message":None})
    
    return render(request,"accounts/dashboard.html")

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

def apply_for_election(request):
    user_id = request.user.id

    try:
        candidate = Candidate.objects.get(student__user__id = user_id)
    except Candidate.DoesNotExist :
        candidate = None
    except Candidate.MultipleObjectsReturned:           #will handle this case later
        candidate = None

    if candidate is None:
        return redirect('profile_image_upload')
    else:
        return redirect('candidate_profile',candidate_id = candidate.id)

def profile_image_view(request):
  
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
  
        user_id = request.user.id
        if form.is_valid():
            
            currobject = form.save()
            student = Student.objects.get(user__id = user_id)
            student.roles.add(2)
            student.save()
            candidate = Candidate()
            candidate.profile = currobject
            candidate.student = Student.objects.get(user__id = user_id)
            candidate.save()
            candidate = Candidate.objects.get(student__user__id = user_id)
            id = candidate.id
            return redirect('candidate_profile',candidate_id = id)
    else:
        form = ProfileForm()
    return render(request, 'accounts/createprofile.html', {'form' : form})

def get_candidate_profile(request,candidate_id):
    candidate = Candidate.objects.get(id = candidate_id)
    context = {
            'candidate' : candidate ,
            'student' : candidate.student ,
            'profile' : candidate.profile
        }
    return render(request,"accounts/candidateprofile.html",context)