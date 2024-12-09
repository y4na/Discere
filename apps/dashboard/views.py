from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfilePictureForm, CustomPasswordChangeForm
from .models import Profile
from .models import ExamSet




# Create your views here.
def dashboard_home(request):
    return render(request, 'dashboard/home.html')





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
def library(request):
    exam_sets = ExamSet.objects.filter(user=request.user)
    return render(request, 'dashboard/library.html', {'exam_sets': exam_sets})

def studysets_view(request):
    return render(request, 'library/studysets.html')

def exams_view(request):
    return render(request, 'library/exams.html')

def exam_creation(request):
    return render(request, 'exams/exam-creation.html')

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


