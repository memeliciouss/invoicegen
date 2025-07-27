from django.db import models

# Create your models here.
class buyer(models.Model):
    buyerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    adr1 = models.CharField(max_length=128)
    adr2 = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=32)
    pin = models.IntegerField()
    gstin = models.CharField(max_length=15)

    def __str__(self):
        return str(self.name) + f"({self.name})"