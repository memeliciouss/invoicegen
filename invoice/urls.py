from django.contrib import admin
from django.urls import path
from invoice import views

urlpatterns = [
    path('generate',views.generate, name='generateInvoice'),
    path('<int:pk>', views.invoiceView, name='invoice'),
    path('drop/<int:pk>',views.drop, name='dropInvoice'),
    path('list',views.invoiceList, name='InvoiceList'),
]