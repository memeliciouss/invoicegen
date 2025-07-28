from django.shortcuts import render, redirect, get_object_or_404
from buyer.models import buyer
from buyer.forms import newBuyerForm

# Create your views here.
def buyers(request):
    context = {
        'buyers':buyer.objects.all()
    }
    return render(request, 'buyers.html', context)

def add(request):
    if request.method=='POST':
        newBuyer = newBuyerForm(request.POST)
        if newBuyer.is_valid():
            newBuyer.save()
            return redirect('/buyers')
    else:
        form = newBuyerForm()
    return render(request, 'addBuyer.html',{'form':form})


def drop(request, pk):
    buyerInst = get_object_or_404(buyer, buyerId = pk)

    if request.method == "POST":
        buyerInst.delete()
        return redirect('/buyers')
    return redirect('/buyers')