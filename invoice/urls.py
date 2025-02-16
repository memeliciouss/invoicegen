from django.contrib import admin
from django.urls import path
from invoice import views

urlpatterns = [
    path('generate',views.generate, name='geninvoice'),
    path('<int:invID>', views.inv, name='inv'),
    path('all', views.all, name='all')
]
