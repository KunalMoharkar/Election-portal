#username -suruchi pwd - django
from django.contrib import admin
from .models import Department, Year, Role, Student, Voter, Profile, Candidate 

# Register your models here.
admin.site.register(Department)
admin.site.register(Year)
admin.site.register(Role)
admin.site.register(Student)
admin.site.register(Voter)
admin.site.register(Profile)
admin.site.register(Candidate)