from django.contrib.auth.models import AbstractUser
from django.db import models

class User_profile(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    adr = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pin = models.CharField(max_length=20, blank=True, null=True)
    company_phone = models.CharField(max_length=20, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)
    gstin = models.CharField(max_length=15, blank=True, null=True, unique=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    bank_acc_no = models.CharField(max_length=50, blank=True, null=True)
    bank_ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    # company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)


    def __str__(self):
        return self.name

# You would NOT include Client, Invoice, InvoiceItem models if you have them handled elsewhere.