from django.urls import path
from . import views

urlpatterns = [
    path('flashcard-creation/', views.flashcard_creation, name='flashcard_creation'),
    path('', views.flashcard_view, name='flashcard_view'), 
    path('flashcards/', views.flashcard_display_view, name='flashcard_display'), 
]