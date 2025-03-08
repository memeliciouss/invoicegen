from django.db import models

#register model in app's admin.py
#add app in project's settings.py 's installed app
#python manage.py makemigratinos
#python manage.py migrate

# Create your models here.
class Buyer(models.Model):
    buyer_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64)
    adr=models.CharField(max_length=128)
    state=models.CharField(max_length=32)
    pin=models.IntegerField()
    gst=models.CharField(max_length=15)

    def __str__(self):
        return str(self.buyer_id) + ": " + self.name
        # it must return a str type