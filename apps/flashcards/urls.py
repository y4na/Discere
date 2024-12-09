from django.urls import path
from . import views

urlpatterns = [
    path('flashcard-creation/', views.flashcard_creation, name='flashcard_creation'),
    path('flashcard-viewer/', views.flashcard_viewer, name='flashcard_viewer'),
    path('flashcard-view/', views.flashcard_view, name='flashcard_view'),
    path('library/', views.library_view, name='library_view'),
    path('delete_flashcards/', views.delete_flashcards, name='delete_flashcards'),
]