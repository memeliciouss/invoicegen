from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.urls import reverse
from .forms import newInvoiceForm, ItemFormSet, editInvoiceForm, ItemEditFormSet
from .models import Invoice

# Create your views here.
@transaction.atomic
def generate(request):
    if request.method=='POST':
        invoiceForm = newInvoiceForm(request.POST)
        itemFormSet = ItemFormSet(request.POST, prefix='items')
        if invoiceForm.is_valid() and itemFormSet.is_valid():
            newInvoice = invoiceForm.save()


            itemFormSet.instance = newInvoice
            itemFormSet.save()

            newInvoice.calculate_totals()
            newInvoice.save(update_fields=['subTotal', 'gstTotal', 'grandTotal'])

            return redirect('/inv/list')
    else:
        invoiceForm = newInvoiceForm()
        itemFormSet = ItemFormSet(prefix='items')
    context = {
        'invoiceForm': invoiceForm,
        'itemFormSet': itemFormSet
    }
    return render(request, 'generateInvoice.html', context)

@transaction.atomic
def edit(request, pk):
    invoiceInst = get_object_or_404(Invoice, invId = pk)
    if request.method=='POST':
        invoiceForm = editInvoiceForm(request.POST, instance = invoiceInst)
        itemFormSet = ItemEditFormSet(request.POST, instance = invoiceInst, prefix='items')
        if invoiceForm.is_valid() and itemFormSet.is_valid():
            invoiceForm.save()
            itemFormSet.save()

            invoiceInst.calculate_totals()
            invoiceInst.save(update_fields=['subTotal', 'gstTotal', 'grandTotal'])

            return redirect(reverse('invoice', args=[pk]))
    else:
        invoiceForm = editInvoiceForm(instance=invoiceInst)
        itemFormSet = ItemEditFormSet(instance=invoiceInst,prefix='items')
    context = {
        'invoiceForm': invoiceForm,
        'itemFormSet': itemFormSet,
        'invoiceInst':invoiceInst
    }
    return render(request, 'editInvoice.html', context)

def invoiceView(request, pk):
    invoiceInst = Invoice.objects.select_related('buyerId').get(invId = pk)
    context = {
        'invoice':invoiceInst,
        'items': invoiceInst.items_set.all()
    }
    return render(request, 'invoice.html',context)

def invoiceList(request):
    context={
        'invoices':Invoice.objects.all().select_related('buyerId')
    }
    return render(request, 'invoiceList.html', context)

def drop(request, pk):
    invoiceInst = get_object_or_404(Invoice, invId = pk)
    if request.method == 'POST':
        invoiceInst.delete()
        return redirect('/inv/list')
    return redirect('/inv/list')