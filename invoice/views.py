from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from invoice.models import Invoice, Items
from buyer.models import Buyer
from invoice.utils import calculate_invoice_total

# Create your views here.

def generate(request):
    if request.method == "POST":

        #get buyer info
        buyer_id=request.POST.get('buyerID')
        buyer_instance=Buyer.objects.get(buyerID=buyer_id)

        #create new invoice
        date=request.POST.get('invoiceDate')
        newInv=Invoice(buyerID=buyer_instance,date=date)
        newInv.save()

        #fetch item details
        item_list=request.POST.getlist('itemName')
        rates=request.POST.getlist('rate')
        gsts=request.POST.getlist('gst')
        qtys=request.POST.getlist('qty')

        for itemName,rate,gst,qty in zip(item_list,rates,gsts,qtys):
            new_item=Items(invID=newInv,itemName=itemName,rate=rate,gst=gst,qty=qty)
            new_item.save()
        return redirect('/inv/list')
    
    context={
        'buyers':Buyer.objects.all()
    }
    return render(request, 'generate.html',context)

def inv(request, invID):
    # invoice_instance=invoice.objects.get(invID=invID)
    invoice_instance=get_object_or_404(Invoice,invID=invID)
    invoice_instance.total=calculate_invoice_total(invID)
    context={
        'invoice':invoice_instance,
        'items':Items.objects.filter(invID=invoice_instance)
        # get: This method returns a single object that matches the given query parameters. If no object or more than one object matches the query, it will raise an error (DoesNotExist or MultipleObjectsReturned, respectively).
        # filter: This method returns a QuerySet containing zero, one, or many objects that match the given query parameters. It does not raise an error if no objects match the query; instead, it simply returns an empty QuerySet.    
    }
    return render(request, 'inv.html', context)

def list(request):
    invoices=Invoice.objects.all()
    for invoice in invoices:
        invoice.total=calculate_invoice_total(invoice.invID)
    context={
        'invoices':invoices,
    }
    return render(request,'invoices.html',context)

def remove(request, invoice_id):
    invoice=get_object_or_404(Invoice, invID=invoice_id)
    if request.method == 'POST':
        invoice.delete()
        return HttpResponse("otw to delete correctly")
    return HttpResponse('otw to delete but off')
