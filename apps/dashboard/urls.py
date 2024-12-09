from django.urls import path
from . import views
from .views import request_email_change, confirm_email_change
from apps.flashcards.views import flashcard_viewer


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
    path('library', views.create_study_set, name='create_study_set'),
    path('create_exam_set/', views.create_exam_set, name='create_exam_set'),
    path('flashcard-viewer/<int:study_set_id>/', flashcard_viewer, name='flashcard_viewer'),
    path("save-exam-set/", views.save_exam_set, name="save_exam_set"),
    # path('create-exam/', views.exam_creation, name='exam_creation'),


    path('create-study-set/dashboard/library', views.library, name='library_dashboard'),
    path('create-study-set/flashcards/flashcard-creation/', views.flashcard_creation, name='flashcard_creation'),
]