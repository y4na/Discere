from django.db import models
from django.contrib.auth.models import User

class StudySet(models.Model):
    set_name = models.CharField(max_length=255)
    set_subject = models.CharField(max_length=255)
    flashcard_count = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.set_name
    
    def get_id(self):
        return self.id
    
    class Meta:
        verbose_name = "Study Set"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='global-images/default-user-profile.png')


class ExamSet(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    exam_type = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_sets')
    exam_card_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def update_exam_card_count(self):
        self.exam_card_count = self.exam_cards.count()
        self.save()
