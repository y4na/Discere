from django.contrib import admin
from .models import Flashcard

@admin.register(Flashcard)
class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'study_set_id', 'study_set', 'term', 'definition', 'isGotIt', 'isNotSure')

    def study_set_id(self, obj):
        return obj.study_set.id
    study_set_id.short_description = 'Study Set ID'
