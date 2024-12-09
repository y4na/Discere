from django.contrib import admin
from .models import StudySet
from apps.flashcards.models import Flashcard
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, ExamSet

@admin.register(StudySet)
class StudySetAdmin(admin.ModelAdmin):
    list_display = ('id', 'set_name', 'set_subject', 'flashcard_count')
    
@admin.register(ExamSet)
class ExamSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'exam_type', 'created_at', 'user')
    search_fields = ('name', 'subject', 'exam_type')  # Enable search by name, subject, and exam_type
    list_filter = ('exam_type', 'subject')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inline_admin_classes = [ProfileInline]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

# Unregister the default User admin
admin.site.unregister(User)
# Register the new User admin
admin.site.register(User, CustomUserAdmin)

# Register the Profile model (add this line)
admin.site.register(Profile)
# admin.site.register(ExamSet)
