from django import forms
from django.forms import inlineformset_factory
from django.forms.widgets import HiddenInput
from django.forms.models import BaseInlineFormSet
from buyer.models import buyer
from user_profile.models import Profile
from invoice.models import Invoice, Items

class newInvoiceForm(forms.ModelForm):
    userId  = forms.ModelChoiceField(
        queryset=Profile.objects.all().order_by('name'),
        label='Select User',
        empty_label='Select User')
    
    buyerId  = forms.ModelChoiceField(
        queryset=buyer.objects.all().order_by('name'),
        label='Select a buyer',
        empty_label='Select a buyer')
    
    class Meta:
        model = Invoice
        
        fields = ['userId','buyerId', 'invNum', 'date']

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
        labels = {
            'itemName':'Item Name',
            'rate':'Rate',
            'gst': 'GST %',
            'qty':'Quantity'
        
        }

class CustomBaseItemFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if 'DELETE' in form.fields:
            form.fields['DELETE'].widget = HiddenInput()

            
ItemFormSet = inlineformset_factory(
    Invoice, 
    Items, 
    form = ItemForm,
    extra = 1,
    min_num=1,
    can_delete=True
)

ItemEditFormSet = inlineformset_factory(
    Invoice, 
    Items,
    form = ItemForm,
    formset=CustomBaseItemFormSet,
    extra = 0,
    min_num=1,
    can_delete=True,
)

class editInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice

        fields = ['invNum', 'date']

        widgets = {
            'date': forms.DateInput(attrs={'type':'date'})
        }

        labels = {
            'invNum': 'Invoice No.',
            'date' : 'Dated',
        }

    def __init__(self, *args, **kwargs):
             
        super().__init__(*args, **kwargs)

        self.fields['invNum'].widget.attrs['readonly'] = True
