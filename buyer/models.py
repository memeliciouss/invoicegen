from django.db import models

#register model in app's admin.py
#add app in project's settings.py 's installed app

# Create your models here.
class buyer(models.Model):
    buyerID=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64)
    adr=models.CharField(max_length=128)
    state=models.CharField(max_length=32)
    pin=models.IntegerField()
    gst=models.CharField(max_length=15)

    def __str__(self):
        return self.buyerID + ": " + self.name
