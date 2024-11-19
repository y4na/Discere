from django.urls import path
from . import views

urlpatterns = [
    path('flashcard-creation/', views.flashcard_creation, name='flashcard_creation'),
    path('flashcard-main/', views.flashcard_main, name='flashcard_main'),
    path('flashcard-base/', views.flashcard_base, name='flashcard_base'),
    path('flashcard-viewer/', views.flashcard_viewer, name='flashcard_viewer'),
    path('', views.flashcard_view, name='flashcard_view'), 
    path('flashcards/', views.flashcard_display_view, name='flashcard_display'), 
]