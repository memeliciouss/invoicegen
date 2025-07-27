from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=128)
    adr1 = models.CharField(max_length=128)
    adr2 = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    pin = models.IntegerField()
    gstin = models.CharField(max_length=15)
    contact = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length = 64,blank=True, null=True)
    bankName = models.CharField(max_length=64)
    bankAcc = models.CharField(max_length=32)
    bandIfsc = models.CharField(max_length=32)
    logo = models.ImageField(upload_to='asset/', blank=True, null=True)

    def __str__(self):
        return self.name