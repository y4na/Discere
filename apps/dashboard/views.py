from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, update_session_auth_hash
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ProfilePictureForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib.auth import login
from django.http import HttpResponse


# Create your views here.
def dashboard_home(request):
    return render(request, 'dashboard/home.html')

@login_required
def user_settings(request):
    current_user = request.user

    profile = current_user.profile  
    form = ProfilePictureForm(instance=profile) 

    if request.method == 'POST' and request.FILES.get('profile_picture'):
        form = ProfilePictureForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save() 
            return redirect('user_settings') 

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

@login_required
def change_password(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user

        # Check current password
        if not user.check_password(current_password):
            messages.error(request, "The current password is incorrect.")
            return redirect("user_settings") 

        # Check if new passwords match
        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return redirect("user_settings")

        # Set the new password
        user.set_password(new_password)
        user.save()

        # Update session hash to keep the user logged in
        update_session_auth_hash(request, user)

        return redirect("user_settings")
    return redirect("user_settings")

@login_required
# def change_username(request):
#     if request.method == "POST":
#         new_username = request.POST.get('new_username')
#         password = request.POST.get('password')
        
#         user = authenticate(username=request.user.username, password=password)
#         if user:
#             if User.objects.filter(username=new_username).exists():
#                 messages.error(request, "Username already taken.")
#             else:
#                 user.username = new_username
#                 user.save()
#                 update_session_auth_hash(request, user)  # Keeps the user logged in
#                 messages.success(request, "Username updated successfully.")
#         else:
#             messages.error(request, "Incorrect password. Please try again.")
    
#     return redirect('user_settings')
def change_username(request):
    if request.method == "POST":
        new_username = request.POST.get("new_username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            # Check if the username is already taken
            if User.objects.filter(username=new_username).exists():
                messages.error(request, "Username is already taken.")
                return redirect("user_settings") 
            user.username = new_username
            user.save()
            return redirect("user_settings")  
        else:
            messages.error(request, "Invalid password. Please try again.")
            return redirect("user_settings") 
    return redirect("user_settings")

email_change_requests = {}

@login_required
def request_email_change(request):
    if request.method == "POST":
        new_email = request.POST.get("new_email")
        password = request.POST.get("password")

        # Authenticate the user's password
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            # Generate a confirmation code
            confirmation_code = random.randint(100000, 999999)
            email_change_requests[request.user.username] = {
                "new_email": new_email,
                "code": confirmation_code,
            }

            # Send the confirmation code to the old email
            send_mail(
                "Email Change Confirmation Code",
                f"Your confirmation code is: {confirmation_code}",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return redirect("confirm_email_change")  # Redirect to confirmation page
        else:
            messages.error(request, "Invalid password. Please try again.")
    return redirect("user_settings")

@login_required
def confirm_email_change(request):
    if request.method == "POST":
        confirmation_code = request.POST.get("confirmation_code")
        user_request = email_change_requests.get(request.user.username)

        if user_request and str(user_request["code"]) == confirmation_code:
            # Update the user's email
            request.user.email = user_request["new_email"]
            request.user.save()

            del email_change_requests[request.user.username]

            return redirect("user_settings")
        
    return render(request, 'dashboard/confirm_email_change.html') 

@login_required
def update_profile(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()

        # Update user's profile
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()

        return redirect("user_settings") 

    return render(request, "dashboard/user_settings.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def delete_account(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Authenticate the user with the provided credentials
        user = authenticate(username=username, password=password)
        
        if user is not None:
            user.delete()
            messages.success(request, "Your account has been deleted successfully.")
            return redirect('home')  # Redirect to the homepage or another page after successful deletion
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('delete_account')

    return redirect('user_settings')
