from django.db import models
from buyer.models import buyer
# Create your models here.
class Invoice(models.Model):
    invId= models.AutoField(primary_key=True)
    invNum = models.CharField(max_length=32)
    buyerId = models.ForeignKey(buyer, on_delete=models.SET_NULL, null=True, blank=True)
    # blank is form level
    # null is databse level
    # making it be null so that deletion can be handfled, but make sure to always pass a buyerId from frontend
    date = models.DateField()

    def __str__(self):
        return str(self.invId)
    
class Items(models.Model):
    invId= models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items_set')
    # deleting referenced object will delete all related objects
    itemName = models.CharField(max_length=64)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=5, decimal_places=2)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return str(self.invId) + f": {self.itemName}"