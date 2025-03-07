from django.db import models

# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=64)
    adr=models.CharField(max_length=255)
    state=models.CharField(max_length=32)
    pin=models.IntegerField()
    gst=models.CharField(max_length=15)
    contact=models.CharField(max_length=64)
    bank_acc=models.IntegerField
    bank_ifsc=models.CharField(max_length=11)

    def __str__(self):
        return self.name
