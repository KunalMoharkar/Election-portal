from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . models import Application, Status
from Election.models import Election
from accounts.models import Candidate, Voter
from Election.views import check_validity
from Election.views import check_timeline
from datetime import date, datetime

# Create your views here.

@login_required
def apply(request,election_id):

    if request.method == "GET":

        election = Election.objects.get(id = election_id)  

        context = {'election':election}  
        #check if the window is open 
        if check_timeline(election_id, 1):
            return render(request,"application/apply.html",context)
        else:
            context = {'message':"Sorry Application window has closed!"}
            return render(request, 'error.html',context)

    else:
        #check if the window is open
        if check_timeline(election_id, 1):
            #check that candidate exists
            user_id = request.user.id
            if Candidate.objects.filter(student__user__id = user_id):

                #now check he is allowed in this election
                voter = Voter.objects.get(student__user__id = user_id)

                if check_validity(voter.id, election_id) == True:
                    
                    msg = request.POST.get('msg')

                    candidate = Candidate.objects.get(student__user__id = user_id)
                    status = Status.objects.get(name = 'in review')
                    application = Application(election_id = election_id, candidate = candidate, status = status, campaign_msg=msg)
                    application.save()
                    context = {'message':"Successfully Applied"}
                    return render(request, 'success.html',context)

                else:
                    context = {'message':"Forbidden", 'code':403}
                    return render(request, 'error.html',context)

            else :

                context = {'message':"Forbidden", 'code':403}
                return render(request, 'error.html',context)
        else:
            context = {'message':"Sorry Application window has closed!"}
            return render(request, 'error.html',context)


@login_required
def my_applications(request):

    user_id = request.user.id
    if Candidate.objects.filter(student__user__id = user_id):
        candidate = Candidate.objects.get(student__user__id = user_id)

        applications = Application.objects.filter(candidate = candidate)

        context = {'applications':applications}

        return render(request,"application/myapplications.html",context)


    else:
        context = {'message':"Forbidden", 'code':403}
        return render(request, 'error.html',context)

