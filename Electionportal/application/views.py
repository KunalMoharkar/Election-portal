from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from . models import Application, Status
from accounts.models import Candidate, Voter
from Election.views import check_validity

# Create your views here.


@login_required
def apply(request,election_id):

    #check that candidate exists
    user_id = request.user.id
    if Candidate.objects.filter(student__user__id = user_id):
        
        #now check he is allowed in this election
        voter = Voter.objects.get(student__user__id = user_id)

        if check_validity(voter.id, election_id) == True:

            candidate = Candidate.objects.get(student__user__id = user_id)
            status = Status.objects.get(name = 'in review')
            application = Application(election_id = election_id, candidate = candidate, status = status, campaign_msg="abc")
            application.save()
            context = {'message':"Successfully Applied"}
            return render(request, 'success.html',context)
        
        else:
            context = {'message':"Forbidden", 'code':403}
            return render(request, 'error.html',context)

    else :

        context = {'message':"Forbidden", 'code':403}
        return render(request, 'error.html',context)