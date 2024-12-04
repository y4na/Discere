from django.contrib import admin
from .models import StudySet
from apps.flashcards.models import Flashcard

@admin.register(StudySet)
class StudySetAdmin(admin.ModelAdmin):
    list_display = ('id', 'set_name', 'set_subject', 'flashcard_count')
    
