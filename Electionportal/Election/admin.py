from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Timestamp)
admin.site.register(Election)
admin.site.register(Votescasted)
admin.site.register(Votesreceived)