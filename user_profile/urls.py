from django.urls import path
from user_profile import views
urlpatterns = [
    path('',views.dashboard, name='Home'),
    path('profile/',views.profile, name='profileView'),
    path('profile/edit/<int:pk>',views.profileEdit, name='profileEdit'),
]