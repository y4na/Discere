from django.urls import path
from . import views

urlpatterns = [
    path('flashcard-creation/', views.flashcard_creation, name='flashcard_creation'),
    path('flashcard-view/', views.flashcard_view, name='flashcard_view'),
    path('flashcard-editor/', views.flashcard_edit_viewer, name='flashcard-editor'),
    path('flashcards/<int:study_set_id>/viewer/', views.flashcard_viewer, name='flashcard_viewer'),
    path('library/', views.library_view, name='library_view'),
    path('delete_flashcards/', views.delete_flashcards, name='delete_flashcards'),
    path('delete-study-set/<int:study_set_id>/', views.delete_study_set, name='delete_study_set'),
]