from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_elections,name="get_elections"),
    path('vote/<int:election_id>/<int:candidate_id>',views.vote_election,name="vote_election"),
    path('results/<int:election_id>',views.election_results,name="election_results"),
]
