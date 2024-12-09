from django.urls import path
from . import views

urlpatterns = [
    path('flashcard-creation/', views.flashcard_creation, name='flashcard_creation'),
    path('flashcard-view/', views.flashcard_view, name='flashcard_view'),
    path('flashcard-result/', views.flashcard_result_viewer, name='flashcard_result_view'),
    path('flashcards/<int:study_set_id>/viewer/', views.flashcard_viewer, name='flashcard_viewer'),
    path('library/', views.library_view, name='library_view'),
    path('delete_flashcards/', views.delete_flashcards, name='delete_flashcards'),
    path('update_flashcard_status/', views.update_flashcard_status, name='update_flashcard_status'),
]