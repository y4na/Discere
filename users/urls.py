from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, PasswordResetDoneView



urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'), 
    
    # Password reset
     path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),  # URL for requesting a password reset
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),  # URL to show after password reset email is sent
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # URL to reset the password
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # URL to show after password has been successfully reset
]

