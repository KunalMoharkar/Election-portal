from django.http.response import HttpResponse
from django.shortcuts import render
from . models import Votesreceived

# Create your views here.


#this view serves the available eletions for a student
#both for application as well as voting 
def get_elections(request):

    #filter on user dept

    #filter on user year
    return HttpResponse("<h1>Get election view</h1>")

#this view increments the vote of a candidate for a 
#particular election
def vote_election(request,election_id,candidate_id):

    #check first that the candidate has not already voted



    #insert voter into votescasted

    return HttpResponse("<h1>vote election view</h1>")

#returns votewise sorted list of candidates
#for a particaluar election
def election_results(request,election_id):
    
    results = Votesreceived.objects.filter(election_id = election_id)

    print(results)


    return render(request,"Election/election-results.html")
