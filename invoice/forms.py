from django import forms
from django.forms import inlineformset_factory
from buyer.models import buyer
from invoice.models import Invoice, Items

class newInvoieceForm(forms.ModelForm):

    buyer  = forms.ModelChoiceField(
        queryset=buyer.objects.all().order_by('name'),
        label='Select a buyer',
        empty_label='Select a buyer')
    class Meta:
        model = Invoice
        
        fields = ['buyer', 'invNum', 'date']

        widgets = {
            'date': forms.DateInput(attrs={'type':'date'})
        }

        labels = {
            'invNum': 'Invoice No.',
            'date' : 'Dated'
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['itemName', 'rate', 'gst', 'qty']
        

ItemFormSet = inlineformset_factory(
    Invoice, 
    Items, 
    form = ItemForm,
    extra = 1,
    can_delete=True
)