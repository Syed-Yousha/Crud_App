from ctypes import addressof
from unicodedata import name
from django.db import models
from django.forms import CharField
from django.db import models

# Create your models here.

class employees(models.Model):
    name = models.CharField(max_length = 200 )
    email = models.EmailField(max_length = 100)
    address = models.TextField()
    phone = models.IntegerField()


    def __str__(self):
        return self.name