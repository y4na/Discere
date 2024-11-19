from django.urls import path
from . import views

urlpatterns = [
    path('discere/home/', views.dashboard_home, name='dashboard_home'),
    path('profile/', views.user_settings, name='user_settings'),
    path('library/', views.library, name='library'),
    path('exams/', views.exams_view, name='exams'),
    path('library', views.create_study_set, name='create_study_set'),
    # Nested path for dashboard and library
    path('create-study-set/dashboard/library', views.library, name='library_dashboard'),
    path('create-study-set/flashcards/flashcard-creation/', views.flashcard_creation, name='flashcard_creation'),
]