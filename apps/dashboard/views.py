from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfilePictureForm


# Create your views here.
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm

@login_required
def user_settings(request):
    current_user = request.user
    form = ProfilePictureForm(instance=current_user)  # Pre-fill the form with the current user's profile picture

    if request.method == 'POST' and request.FILES.get('profile_picture'):
        form = ProfilePictureForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()  # Save the updated profile picture
            return redirect('user_settings')  # Redirect back to the user settings page

    context = {
        'user': current_user,
        'form': form
    }
    return render(request, 'dashboard/user_settings.html', context)


    
def library(request):
    return render(request, 'dashboard/library.html')

def studysets_view(request):
    return render(request, 'library/studysets.html')

def exams_view(request):
    return render(request, 'library/exams.html')

# def user_settings(request):
#     # Make sure the user is authenticated
#     if not request.user.is_authenticated:
#         return redirect('login')

#     user_profile = UserProfile.objects.get(user=request.user)

#     if request.method == 'POST':
#         form = ProfilePictureForm(request.POST, request.FILES)
#         if form.is_valid():
#             user_profile.profile_picture = form.cleaned_data['profile_picture']
#             user_profile.save()

#             messages.success(request, 'Your profile picture has been updated!')
#             return redirect('user_settings') 
#     else:
#         form = ProfilePictureForm(instance=user_profile)

#     return render(request, 'dashboard/user_settings.html', {'form': form})
