from asyncio.windows_events import NULL
import email
from django.db import models
from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pickle import TRUE
from unicodedata import name
from zoneinfo import available_timezones
from django.db import models


class Owners(models.Model):
    name = models.CharField(max_length=30, unique=False)
    surname = models.CharField(max_length=30, unique=False, null=True)
    contact = models.CharField(max_length=30, unique=False, null=True)
    phone_number = models.IntegerField(blank=True)
    email = models.EmailField(max_length=254,null=True)
    # Media part of Model
    # image=models.ImageField(upload_to="anımals/%Y/%m/%d/")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

# __str__ method  returns Owners Class

def __str__(self):
    return self.name


#ad soyad, iletişim bilgileri, telefon,e-posta
