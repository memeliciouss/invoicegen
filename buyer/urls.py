from django.contrib import admin
from django.urls import path
from buyer import views

urlpatterns = [
    path('',views.buyers, name='buyers'),
    path('add', views.add, name='addBuyer')
]
