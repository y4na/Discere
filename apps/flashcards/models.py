from django.db import models
from apps.dashboard.models import StudySet

class Flashcard(models.Model):
    study_set = models.ForeignKey(StudySet, related_name='flashcards', on_delete=models.CASCADE)
    term = models.CharField(max_length=200)
    definition = models.TextField()

    def __str__(self):
        return self.term
