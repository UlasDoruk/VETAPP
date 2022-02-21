from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pickle import TRUE
from pyexpat import model
from unicodedata import name
from zoneinfo import available_timezones
from django.db import models
from owners.models import Owners

class Anımals(models.Model): 
    # owner field bounded to Anımals model. I choosed CASCADE method to on_delete field. Beacuse if we delete the owner, then we delete to animal which is owner's have
    owner = models.ForeignKey(Owners,null=True,on_delete=models.CASCADE)
    name= models.CharField(max_length=30, unique=True)
    type = models.CharField(max_length=30, unique=False,null=True)
    species = models.CharField(max_length=30, unique=False,null=True)
    age = models.IntegerField( unique=False,null=True)
    description= models.TextField(blank=True,null=True)
    # Media part of Anımals model 
    # image=models.ImageField(upload_to="anımals/%Y/%m/%d/") 
    date=models.DateTimeField( auto_now=True)
    available=models.BooleanField(default=True)
    
# Returning Anımals Class
    def __str__(self):
        return self.name


# tür, cins, isim, yaş, açıklama 
