from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('profile/',views.profile, name='dashboard'),
]
