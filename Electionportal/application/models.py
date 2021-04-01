from django.db import models
from Election.models import Election
from accounts.models import Candidate

# Create your models here.


class Status(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Application(models.Model):

    election = models.ForeignKey(Election, on_delete= models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete= models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    date_of_application = models.DateField()
    campaign_msg = models.TextField()

    def __str__(self):
        return self.candidate.student.user.username
