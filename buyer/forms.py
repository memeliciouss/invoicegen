from django import forms
from buyer.models import buyer

class newBuyerForm(forms.ModelForm):
    class Meta:
        model  = buyer
        fields = ['name', 'adr1', 'adr2', 'state', 'pin', 'gstin']
        # fields = '__all__'
        labels = {
            'name': 'Name',
            'adr1': 'Address Line 1',
            'adr2': 'Address Line 2',
            'state': 'State',
            'pin': 'PIN Code',
            'gstin': 'GSTIN'
        }