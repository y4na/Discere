from django.urls import path
from . import views

urlpatterns = [
    path('', views.flashcard_view, name='flashcard_view'), 
    path('flashcards/', views.flashcard_display_view, name='flashcard_display'), 
]
