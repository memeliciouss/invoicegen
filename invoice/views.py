from django.shortcuts import render, redirect, get_object_or_404
from invoice.models import Invoice, Items
from buyer.models import Buyer
from invoice.utils import calculate_invoice_total

# Create your views here.

def generate(request):
    if request.method == "POST":

        #get buyer info
        buyerID=request.POST.get('buyerID')
        buyer_instance=Buyer.objects.get(buyer_id=buyerID)

        #create new invoice
        date=request.POST.get('invoiceDate')
        newInv=Invoice(buyer_id=buyer_instance,date=date)
        newInv.save()

        #fetch item details
        item_list=request.POST.getlist('itemName')
        rates=request.POST.getlist('rate')
        gsts=request.POST.getlist('gst')
        qtys=request.POST.getlist('qty')

        for itemName,rate,gst,qty in zip(item_list,rates,gsts,qtys):
            new_item=Items(inv_id=newInv,item_name=itemName,rate=rate,gst=gst,qty=qty)
            new_item.save()
        return redirect('/inv/list')
    
    context={
        'buyers':Buyer.objects.all()
    }
    return render(request, 'generate.html',context)

def inv(request, invID):
    # invoice_instance=invoice.objects.get(invID=invID)
    invoice_instance=get_object_or_404(Invoice,inv_id=invID)
    invoice_instance.total=calculate_invoice_total(invID)
    items=Items.objects.filter(inv_id=invoice_instance)
    for item in items:
        item.amount=item.qty*item.rate
    context={
        'invoice':invoice_instance,
        'items':items
        # get: This method returns a single object that matches the given query parameters. If no object or more than one object matches the query, it will raise an error (DoesNotExist or MultipleObjectsReturned, respectively).
        # filter: This method returns a QuerySet containing zero, one, or many objects that match the given query parameters. It does not raise an error if no objects match the query; instead, it simply returns an empty QuerySet.    
    }
    return render(request, 'inv.html', context)

def list(request):
    invoices=Invoice.objects.all()
    for invoice in invoices:
        invoice.total=calculate_invoice_total(invoice.inv_id)
    context={
        'invoices':invoices,
    }
    return render(request,'invoices.html',context)

def remove(request, invoice_id):
    invoice=get_object_or_404(Invoice, inv_id=invoice_id)
    if request.method == 'POST':
        invoice.delete()
        return redirect('list')
    return redirect('list')
