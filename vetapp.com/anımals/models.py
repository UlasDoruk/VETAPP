from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pickle import TRUE
from unicodedata import name
from zoneinfo import available_timezones
from django.db import models

class Anımals(models.Model):
    name= models.CharField(max_length=30, unique=True,verbose_name="Animals")
    description= models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to="anımals/%Y/%m/%d/")
    date=models.DateTimeField( auto_now=True)
    available=models.BooleanField(default=True)

