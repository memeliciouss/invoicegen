from django.contrib import admin
from django.urls import path
from invoice import views

urlpatterns = [
    path('generate',views.generate, name='geninvoice'),
    path('<int:invID>', views.inv, name='inv'),
    path('list', views.list, name='list'),
    path('remove/<int:invoice_id>', views.remove, name='remove')
]
