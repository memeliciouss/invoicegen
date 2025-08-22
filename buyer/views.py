from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from buyer.models import buyer
from buyer.forms import newBuyerForm

# Create your views here.
def buyers(request):
    buyers=buyer.objects.all().order_by('buyerId')
    paginator = Paginator(buyers, 10)
    page_number = request.GET.get('page')
    buyers_page = paginator.get_page(page_number
                                     )
    context = {
        'buyers': buyers_page
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