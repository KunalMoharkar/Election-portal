from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Election, Votesreceived, Votescasted
from accounts.models import Voter, Student
from django.contrib.auth.decorators import login_required

# Create your views here.

#helper function to determine if a election is open for a student
def check_validity(voter_id, election_id):

    election = Election.objects.get(id = election_id)
    voter = Voter.objects.get(id = voter_id)

    voter_year = voter.student.year.name
    voter_dept = voter.student.department.code

    print(voter_year)
    print(voter_dept)

    allowed_depts = election.allowed_depts.all()
    allowed_years = election.allowed_years.all()

    dept_list = []
    year_list = []

    for x in allowed_depts:
        dept_list.append(x.code)
    
    for x in allowed_years:
        year_list.append(x.name)
    
    print(dept_list)
    print(year_list)

    #cleck for year and dept also
    if (voter_year in year_list) and (voter_dept in dept_list):

        print('allowed')
        return True 

    return False

#this view serves the available eletions for a student
#both for application as well as voting 

@login_required
def get_elections(request):

    student = Student.objects.get(user = request.user)

    elections = Election.objects.filter(allowed_depts__code = student.department.code, allowed_years__name = student.year.name)
    
    context = {'elections':elections}

    print(elections)

    return render(request,'Election/all-elections.html',context)

#this view increments the vote of a candidate for a 
#particular election

@login_required
def vote_election(request,election_id,candidate_id):

    #check first that the candidate has not already voted

    user_id = request.user.id

    voter = Voter.objects.get(student__user__id = user_id)

    if not Votescasted.objects.filter(voter_id = voter.id, election_id = election_id):
        
        #now check that voter can vote in that election
        if check_validity(voter.id,election_id) == True:

            #add vote
            votesrec = Votesreceived.objects.get(election_id = election_id, candidate_id = candidate_id)
            votesrec.votes = votesrec.votes + 1
            votesrec.save()

            #register that voter has voted
            votescasted = Votescasted(voter_id = voter.id, election_id = election_id)
            votescasted.save()

            context = {'message':"Vote has been successfully recorded"}
            return render(request, 'success.html',context)

        else:
            context = {'message':"Forbidden", 'code':403}
            return render(request,'error.html',context)
        
    else:
        context = {'message':"Forbidden - already voted", 'code':403}
        return render(request, 'error.html',context)

#returns votewise sorted list of candidates
#for a particaluar election

@login_required
def election_results(request,election_id):
    
    results = Votesreceived.objects.filter(election_id = election_id).order_by('-votes')
    context = {'results':results}

    return render(request,"Election/election-results.html",context)
