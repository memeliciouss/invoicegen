from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ProfileEditForm
from .models import Profile
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def profile(request):
    context={
    'profiles': Profile.objects.all()
    }
    return render(request, 'profiles.html', context)



def profileEdit(request, pk):
    profile = get_object_or_404(Profile, userId = pk)
    if request.method == 'POST':
        profileForm = ProfileEditForm(request.POST, instance = profile)
        if profileForm.is_valid():
            profileForm.save()
            return redirect(reverse('profileView'))
    else:
        profileForm = ProfileEditForm(instance=profile)
    context = {
        'form':profileForm
    }
    return render(request, 'profileEdit.html', context)