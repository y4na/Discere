from django.contrib import admin
from .models import Flashcard

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'study_set', 'term', 'definition')  # Fields to display in the list view
