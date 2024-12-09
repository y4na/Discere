from django.db import models
from apps.dashboard.models import ExamSet

class ExamCard(models.Model):
    term = models.CharField(max_length=255)
    definition = models.TextField()
    exam_set = models.ForeignKey(ExamSet, on_delete=models.CASCADE, related_name='exam_cards')

    def __str__(self):
        return self.term