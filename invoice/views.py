from django.shortcuts import render, redirect
from invoice.models import invoice
from buyer.models import buyer

# Create your views here.

def generate(request):
    if request.method == "POST":
        buyer_id=request.POST.get('buyerID')
        buyer_instance=buyer.objects.get(buyerID=buyer_id)
        newInv=invoice(buyerID=buyer_instance)
        newInv.save()

        return redirect('/inv/all')
    
    context={
        'buyers':buyer.objects.all()
    }
    return render(request, 'generate.html',context)

def inv(request, invID):
    invoice_instance=invoice.objects.get(invID=invID)
    context={
        'invoices':invoice_instance
    }
    return render(request, 'invoices.html', context)

def all(request):
    context={
        'invoices':invoice.objects.all()
    }
    return render(request,'invoices.html',context)
