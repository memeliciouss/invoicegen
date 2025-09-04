from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    context={
    'profiles': Profile.objects.all()
    }
    return render(request, 'profiles.html', context)

def profileCreate(request):
    profileForm = ProfileForm()
    context ={
        'form':profileForm,
        'title':'Create New Profile'
    }
    return render(request, 'profileForm.html', context)

def profileEdit(request, pk):
    profile = get_object_or_404(Profile, userId = pk)
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, request.FILES, instance = profile)
        if profileForm.is_valid():
            profileForm.save()
            return redirect(reverse('profileView'))
    else:
        profileForm = ProfileForm(instance=profile)
    context = {
        'form':profileForm,
        'title':f'Edit Profile ({pk})'
    }
    return render(request, 'profileForm.html', context)