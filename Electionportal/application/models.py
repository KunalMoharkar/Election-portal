from django.db import models
from Election.models import Election, Votesreceived
import datetime
from accounts.models import Candidate
from django.conf import settings
from django.core.mail import send_mail

# Create your models here.


class Status(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Application(models.Model):

    election = models.ForeignKey(Election, on_delete= models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete= models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    date_of_application = models.DateField(default=datetime.date.today)
    campaign_msg = models.TextField()

    def __str__(self):
        return self.candidate.student.user.username
    
    def save(self, *args, **kwargs):
        subject = 'Welcome to Election portal'
        message = f'Hi {self.candidate.student.user.username}, your application status is {self.status}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.candidate.student.user.email, ]
        send_mail( subject, message, email_from, recipient_list )
        
        if self.status.name == "accepted":
            newCandidate = Votesreceived(election = self.election, candidate = self.candidate, votes = 0)
            newCandidate.save()
        super(Application, self).save(*args, **kwargs)
