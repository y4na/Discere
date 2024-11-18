from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.http import JsonResponse
import json
from django.contrib.auth.models import User


# Create your views here.
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

def user_settings(request):
        user = request.user  
        context = {
            'user': user 
        }
        return render(request, 'dashboard/user_settings.html')

@login_required
def user_profile(request):
    user = request.user
    user_profile = user.userprofile
    reading_activity = user_profile.reading_activity.all()  
    achievements = user_profile.achievements.all()  

    context = {
        'user': user,
        'reading_activity': reading_activity,
        'achievements': achievements,
    }
    return render(request, 'dashboard/user_settings.html', context)


    
def library(request):
    return render(request, 'dashboard/library.html')

def studysets_view(request):
    return render(request, 'library/studysets.html')

def exams_view(request):
    return render(request, 'library/exams.html')

