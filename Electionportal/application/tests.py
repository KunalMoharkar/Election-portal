from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from .models import Application, Status
from accounts.models import Student, Candidate, Role, Year, Department, Profile
from django.contrib.auth.models import User


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


    
    def test_insertion(self):
        self.assertEqual(Student.objects.count(), 1)
  



