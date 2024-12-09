from django.urls import path
from . import views
from apps.flashcards.views import flashcard_viewer

urlpatterns = [
    path('discere/home/', views.dashboard_home, name='dashboard_home'),
    path('profile/', views.user_settings, name='user_settings'),
    path('library/', views.library, name='library'),
    path('exams/', views.exams_view, name='exams'),
]