from django.contrib import admin
from django.urls import path
from dashboard import views

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('profile', views.profile, name='profile')
]
