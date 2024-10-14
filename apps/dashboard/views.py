from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
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

