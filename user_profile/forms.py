from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'name': 'Name',
            'adr1': 'Address Line 1',
            'adr2': 'Address Line 2',
            'state': 'State',
            'pin': 'PIN Code',
            'gstin': 'GSTIN',
            'contact':'Contact',
            'email':'E-Mail address',
            'bankName':'Bank Name',
            'bankAcc':'Account Number',
            'bankIfsc':'IFSC Code',
            'logo':'Logo'
        }