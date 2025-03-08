from django.shortcuts import render, redirect, get_object_or_404
from buyer.models import Buyer
from django.http import HttpResponse

# Create your views here.
def buyers(request):
    buyers=Buyer.objects.all()
    context={
        'buyers':buyers
    }
    return render(request, 'buyers.html',context)

def add(request):
    if request.method == "POST":
        name = request.POST.get('buyerName')
        adr = request.POST.get('adr')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        gst = request.POST.get('gst')
        new_buyer=Buyer(name=name, adr=adr, state=state, pin=pin, gst=gst)
        new_buyer.save()

        return redirect('/buyers')
    return render(request, 'addBuyer.html')

def remove_buyer(request, buyerID):


    buyer=get_object_or_404(Buyer, buyer_id=buyerID)
    if request.method == 'POST':
        buyer.delete()
        return redirect('buyers')
    return redirect('buyers')