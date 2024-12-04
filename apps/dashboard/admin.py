from django.contrib import admin
from .models import StudySet

@admin.register(StudySet)
class StudySetAdmin(admin.ModelAdmin):
    list_display = ('id', 'set_name', 'set_subject')  # Specify the fields to display in the admin list
