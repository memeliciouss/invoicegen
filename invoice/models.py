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

    subTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    gstTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    grandTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return str(self.invId)
    
    def calculate_totals(self):
        curr_subTotal = 0
        curr_gstTotal = 0

        for item in self.items_set.all():
            curr_subTotal += item.rate * item.qty
            curr_gstTotal += (item.rate * item.qty) * ( item.gst / 100 )

        self.subTotal = round(curr_subTotal, 2)
        self.gstTotal = round(curr_gstTotal, 2)
        self.grandTotal = round( curr_subTotal + curr_gstTotal, 2) 
    
class Items(models.Model):
    invId= models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items_set')
    # deleting referenced object will delete all related objects
    itemName = models.CharField(max_length=64)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    gst = models.DecimalField(max_digits=5, decimal_places=2, default= 18)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return str(self.invId) + f": {self.itemName}"