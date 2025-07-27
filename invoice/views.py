from django.shortcuts import render, redirect

# Create your views here.
def generate(request):
    return render(request, 'generateInvoice.html')

def invoiceView(request):
    return render(request, 'invoice.html')

def invoiceList(request):
    return render(request, 'invoiceList.html')

def drop(request):
    return redirect('/list')