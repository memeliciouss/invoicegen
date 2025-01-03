from django.shortcuts import render, redirect
from buyer.models import buyer

# Create your views here.
def buyers(request):
    buyers=buyer.objects.all()
    return render(request, 'buyers.html', {'buyers':buyers})

def add(request):
    if request.method == "POST":
        name = request.POST.get('buyerName')
        adr = request.POST.get('adr')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        gst = request.POST.get('gst')
        newBuyer=buyer(name=name, adr=adr, state=state, pin=pin, gst=gst)
        newBuyer.save()

        return redirect('/buyers')
    return render(request, 'addBuyer.html')