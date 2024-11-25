from django.db import models
from apps.dashboard.models import StudySet  # Import the StudySet model

class Flashcard(models.Model):
    study_set = models.ForeignKey(  # Establish the ForeignKey relationship
        StudySet, 
        on_delete=models.CASCADE,  # Delete flashcards if the study set is deleted
        related_name='flashcards',
        default=1  # Optional: Allows reverse relationship access
    )
    term = models.CharField(max_length=200)
    definition = models.TextField()

    def __str__(self):
        return self.term
