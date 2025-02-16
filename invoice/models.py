from django.db import models
from buyer.models import buyer

# Create your models here.
class invoice(models.Model):
    invID=models.AutoField(primary_key=True)
    buyerID=models.ForeignKey(buyer,on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.invID