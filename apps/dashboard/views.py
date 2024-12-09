from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfilePictureForm, CustomPasswordChangeForm
from .models import Profile, ExamSet, StudySet
from apps.flashcards.models import Flashcard


def dashboard_home(request):
    # Fetch the most recent study sets
    recent_study_sets = StudySet.objects.all().order_by('-created_date')[:5]

    # Initialize an empty list to store results for the recent study sets
    study_set_results = []

    # Retrieve recent quiz results from the session if available
    recent_study_set = request.session.get('recent_study_set', None)

    # Include the results in the context if available
    if recent_study_set:
        study_set_results.append({
            'study_set': recent_study_set['set_name'],
            'correct_count': recent_study_set['correct_count'],
            'mistake_count': recent_study_set['mistake_count'],
            'total_flashcards': recent_study_set['total_flashcards'],
            'percentage': recent_study_set['overall_score'],
        })

    # Pass the study set results and user data to the template context
    context = {
        'recent_study_sets': recent_study_sets,
        'user': request.user,
        'study_set_results': study_set_results,
    }

    return render(request, 'dashboard/home.html', context)






@login_required
def user_settings(request):
    current_user = request.user
    profile = current_user.profile
    form = ProfilePictureForm(instance=profile)
    password_form = CustomPasswordChangeForm(user=current_user)

    # Handle profile picture change
    if request.method == 'POST' and 'profile_picture' in request.FILES:
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile picture has been updated successfully.")
            return redirect('user_settings')

    # Handle password change
    if request.method == 'POST' and 'current_password' in request.POST:
        password_form = CustomPasswordChangeForm(user=current_user, data=request.POST)
        if password_form.is_valid():
            new_password = password_form.cleaned_data['new_password']
            current_user.set_password(new_password)
            current_user.save()
            update_session_auth_hash(request, current_user)
            messages.success(request, "Your password has been updated successfully.")
            return redirect('user_settings')

    return render(request, 'dashboard/user_settings.html', {
        'form': form,
        'password_form': password_form,
    })


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
    return render(request, 'dashboard/user_profile.html', context)


# Library Views
@login_required
def library(request):
    exam_sets = ExamSet.objects.filter(user=request.user)
    study_sets = StudySet.objects.filter(user=request.user)
    return render(request, 'dashboard/library.html', {'exam_sets': exam_sets, 'study_sets': study_sets})


def studysets_view(request):
    study_sets = StudySet.objects.all()
    return render(request, 'library/studysets.html', {'study_sets': study_sets})


def exams_view(request):
    return render(request, 'library/exams.html')

def exam_creation(request):
    return render(request, 'exams/exam-creation.html')


# Study Set Creation
def create_study_set(request):
    if request.method == 'POST':
        set_name = request.POST.get('study_set_name')
        set_subject = request.POST.get('subject')

        if set_name and set_subject:
            study_set = StudySet.objects.create(set_name=set_name, set_subject=set_subject)

            # Pass the created study set's id to the template
            context = {
                'study_set': study_set,  # Pass the full object for flexibility
            }
            return render(request, 'flashcards/flashcard-creation.html', context)

    return redirect('library')


# Flashcard Views
def flashcard_creation(request):
    return render(request, 'flashcards/flashcard-creation.html')


def flashcard_creation_main(request):
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation-main.html', {'study_sets': study_sets})

@login_required
def create_exam_set(request):
    if request.method == 'POST':
        # Handle the form submission from the front end
        set_name = request.POST.get('exam_set_name')
        subject = request.POST.get('subject')
        exam_type = request.POST.get('exam_type')

        # Create the exam set if all fields are provided
        if set_name and subject and exam_type:
            exam_set = ExamSet.objects.create(
                name=set_name,
                subject=subject,
                exam_type=exam_type,
                user=request.user  # Associate the exam set with the logged-in user
            )

            # You can also pass the created exam set to the template
            context = {
                'exam_set': exam_set,
            }

            # Redirect to exam creation page or render the page
            return render(request, 'exams/exam-creation.html', context)

    # If the form wasn't submitted, show the exam creation page
    return render(request, 'exams/exam-creation.html')


# Exam Set Management
@login_required
def save_exam_set(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            exam_set = ExamSet.objects.create(
                name=data["name"],
                subject=data["subject"],
                exam_type=data["type"],
                user=request.user
            )
            return JsonResponse({"success": True, "exam_set_id": exam_set.id})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request method."})
