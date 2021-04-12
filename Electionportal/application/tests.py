from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from .models import Application, Status
from accounts.models import Student, Candidate, Role, Year, Department, Profile, Voter
from Election.models import Election, Timestamp
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

class ApplicationTestCase(TestCase):

    def setUp(self):

        user = User.objects.create_user('testuser', 'testuser@test.com', 'testpassword')
        year = Year.objects.create(name="third")
        role = Role.objects.create(name='candidate')
        department = Department.objects.create(code='CSE', name='Computer Science') 
        student = Student.objects.create(user = user, department = department,year= year, contact='9325598530')
        student.roles.add(role)
        profile = Profile.objects.create(linkedin_url="https://www.google.com")
        candidate = Candidate.objects.create(student = student, profile = profile)
        voter = Voter.objects.create(student = student)

        application_win = Timestamp.objects.create(election_name='test election 1',start_time =timezone.now(), end_time =timezone.now(),
                                                    start_date=datetime.date.today(),end_date=datetime.date.today())
        
        voting_win = Timestamp.objects.create(election_name='test election 1',start_time =timezone.now(), end_time =timezone.now(),
                                                    start_date=datetime.date.today(),end_date=datetime.date.today())


        election = Election.objects.create(title="test election 1",application_win=application_win, voting_win= voting_win)
        election.allowed_depts.add(department)
        election.allowed_years.add(year)
        status_inreview = Status.objects.create(name='in review')
        status_approved = Status.objects.create(name='approved') 

    def test_apply_view(self):

        self.client.login(username='testuser', password='testpassword')

        message = 'my election test message'
        election = Election.objects.get(id = 1)

        #get request
        response = self.client.get(f'/application/apply/{election.id}')

        self.assertEqual(response.status_code,200)

        #same elction returned
        self.assertEqual(response.context['election'].id,election.id)

        #post request
        response = self.client.post(f'/application/apply/{election.id}',
                                        {'msg':message})

        self.assertEqual(response.status_code,200)
        #object sucessfully inserted
        self.assertEqual(Application.objects.count(),1)
        #check message set properly
        application = Application.objects.get(id = 1)
        self.assertEqual(application.campaign_msg,message)
        #check status set properly
        status = Status.objects.get(name='in review')
        self.assertEqual(application.status.name,status.name)
        #redirection successful
        self.assertEqual(response.context['message'],"Successfully Applied")

    def test_my_aplications_view(self):
        
        
        
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/application/myapplications/')
        self.assertEqual(response.status_code, 200)

        #no application is applied by the voter
        self.assertEqual(response.context['applications'].count(),0)



