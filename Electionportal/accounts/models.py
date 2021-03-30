from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Department(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.name})"

class Year(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} ({self.name})"

class Role(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id} ({self.name})"

class Student(models.Model):
    user = models.OneToOneField(User, 
          on_delete = models.CASCADE)
    department = models.ForeignKey(Department,on_delete = models.CASCADE, related_name="Dept_Students")
    year = models.ForeignKey(Year,on_delete = models.CASCADE, related_name="Students")
    roles = models.ManyToManyField(Role,related_name="Members")
    contact = models.CharField(max_length=20)

class Voter(models.Model):
    student = models.OneToOneField(Student,on_delete = models.CASCADE)

class Profile(models.Model):
    image = models.FileField(upload_to='images/')
    linkedin_url = models.URLField(max_length = 200)

class Candidate(models.Model):
    student = models.OneToOneField(Student,on_delete = models.CASCADE)
    profile = models.OneToOneField(Profile,on_delete = models.CASCADE)
