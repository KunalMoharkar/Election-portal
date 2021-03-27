from django.db import models
from django.db.models.deletion import DO_NOTHING
from accounts.models import Year, Department, Voter, Candidate
# Create your models here.

class Timestamp(models.Model):
    election_name = models.CharField(max_length=1000)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.election_name

class Election(models.Model):
    title = models.CharField(max_length=1000)
    allowed_depts = models.ManyToManyField(Department)
    allowed_years = models.ManyToManyField(Year)
    application_win = models.OneToOneField(Timestamp, on_delete=models.DO_NOTHING, related_name='application_timestamp')
    voting_win = models.OneToOneField(Timestamp,on_delete=models.DO_NOTHING, related_name='voting_timestamp')

    def __str__(self):
        return self.title

class Votescasted(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
        return self.election.title

class Votesreceived(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.election.title
