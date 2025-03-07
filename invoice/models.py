from django.db import models
from buyer.models import Buyer

# Create your models here.
class Invoice(models.Model):
    invID=models.AutoField(primary_key=True)
    buyerID=models.ForeignKey(Buyer,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.invID)
    
class Items(models.Model):
    invID=models.ForeignKey(Invoice,  on_delete=models.CASCADE)
    #deleting the referenced object will delete all the related objects

    itemName=models.CharField(max_length=100)
    rate=models.DecimalField(max_digits=4,decimal_places=2)
    gst=models.DecimalField(max_digits=4,decimal_places=2)
    qty=models.IntegerField(default=1)
    
    def __str__(self):
        return str(self.invID) + ": " +  self.itemName
