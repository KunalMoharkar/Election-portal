from django.urls import path
from . import views

urlpatterns = [
    path('apply/<int:election_id>',views.apply,name="apply_election"),
    path('myapplications/',views.my_applications,name="my_applications"),
]

