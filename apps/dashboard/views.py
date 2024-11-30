from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StudySet

# General Views
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

@login_required
def user_settings(request):
    return render(request, 'dashboard/user_settings.html')

@login_required
def user_profile(request):
    user = request.user
    user_profile = getattr(user, 'userprofile', None)
    reading_activity = user_profile.reading_activity.all() if user_profile else []
    achievements = user_profile.achievements.all() if user_profile else []

    context = {
        'user': user,
        'reading_activity': reading_activity,
        'achievements': achievements,
    }
    return render(request, 'dashboard/user_settings.html', context)

# Library Views
def library(request):
    study_sets = StudySet.objects.all()
    return render(request, 'dashboard/library.html', {'study_sets': study_sets})

def studysets_view(request):
    study_sets = StudySet.objects.all() 
    return render(request, 'library/studysets.html', {'study_sets': study_sets})

def exams_view(request):
    return render(request, 'library/exams.html')

# Study Set Creation
def create_study_set(request):
    if request.method == 'POST':
        set_name = request.POST.get('study_set_name')
        set_subject = request.POST.get('subject')

        if set_name and set_subject:
            study_set = StudySet.objects.create(set_name=set_name, set_subject=set_subject)
            context = {
                'set_name': study_set.set_name,
                'set_subject': study_set.set_subject,
            }

            return render(request, 'flashcards/flashcard-creation.html', context)

    return redirect('library')

# Flashcard Views
def flashcard_creation(request):
    return render(request, 'flashcards/flashcard-creation.html')

def flashcard_creation_main(request):
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation-main.html', {'study_sets': study_sets})
