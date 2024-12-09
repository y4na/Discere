from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='global-images/default-user-profile.png')


class ExamSet(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    subject = models.CharField(max_length=255, null=False, blank=False)
    exam_type = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_sets')
    def __str__(self):
        return self.name