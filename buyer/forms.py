from django import forms
from buyer.models import buyer

class newBuyerForm(forms.ModelForm):
    class Meta:
        model  = buyer
        fields = ['name', 'adr1', 'adr2', 'state', 'pin', 'gstin']
        # fields = '__all__'