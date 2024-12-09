from django.urls import path
from . import views
from .views import request_email_change, confirm_email_change

urlpatterns = [
    path('discere/home/', views.dashboard_home, name='dashboard_home'),
    path('profile/', views.user_settings, name='user_settings'),
    path('library/', views.library, name='library'),
    path('exams/', views.exams_view, name='exams'),
    path("change-password/", views.change_password, name="change_password"),
    path('change-username/', views.change_username, name='change_username'),
    path("change-email/", request_email_change, name="change_email"),
    path("confirm-email-change/", confirm_email_change, name="confirm_email_change"),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('delete_account/', views.delete_account, name='delete_account'),
]
