from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name    =   models.CharField(max_length=100)
    street  =   models.CharField(max_length=100, null=True)
    city    =   models.CharField(max_length=20, null=True)
    state1  =   models.CharField(max_length=20, null=True)
    zipcode =   models.CharField(max_length=15, null=True)
    mobile  =   models.CharField(max_length=15)
    email   =   models.CharField(max_length=20)
    make    =   models.CharField(max_length=20, null=True)
    model   =   models.CharField(max_length=20, null=True)
    series  =   models.CharField(max_length=20, null=True)
    vin     =   models.CharField(max_length=20, null=True)
    lic     =   models.CharField(max_length=20, null=True)
    state   =   models.CharField(max_length=20, null=True)
    memo    =   models.TextField(max_length=100, blank=True)
   
    def __str__(self):
        return self.name



