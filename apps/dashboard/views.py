from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

def user_settings(request):
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

#def library(request):
    #return render(request, 'dashboard/library.html')

def studysets_view(request):
    return render(request, 'library/studysets.html')

def exams_view(request):
    return render(request, 'library/exams.html')

from .models import StudySet

def library(request):
    study_sets = StudySet.objects.all()
    return render(request, 'dashboard/library.html', {'study_sets': study_sets})

def create_study_set(request):
    if request.method == 'POST':
        name = request.POST.get('study_set_name')
        subject = request.POST.get('subject')

        if name and subject:
            StudySet.objects.create(name=name, subject=subject)
            #return redirect('dashboard/library')
            #return redirect('flashcard_creation')
            context = {
                'set_name': name,
                'set_subject': subject,
            }
            return render(request, 'flashcards/flashcard-creation.html', context)

    return render(request, 'dashboard/library.html')

def flashcard_creation(request):
    return render(request, 'flashcards/flashcard-creation.html')




