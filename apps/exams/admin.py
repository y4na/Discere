from django.contrib import admin
from .models import ExamSet, ExamCard
from django.contrib.auth import get_user_model

@admin.register(ExamCard)
class ExamCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'term', 'definition', 'exam_set')  # Display term, definition, and associated exam set
    search_fields = ('term', 'definition')  # Enable search by term and definition
    list_filter = ('exam_set',)
