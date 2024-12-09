from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('password-reset/', views.send_verification_code, name='password_reset'),
    path('verify-code/', views.verify_code, name='verify_code'),
    path('password-reset/', views.send_verification_code, name='send_verification_code'),
    path('reset-password/<str:email>/', views.update_password, name='update_password'),  # Pass email via URL
]
