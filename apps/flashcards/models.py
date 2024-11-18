from django.db import models

class FlashcardSet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    flashcard_set = models.ForeignKey(FlashcardSet, related_name='flashcards', on_delete=models.CASCADE)
    term = models.CharField(max_length=200)
    definition = models.TextField()

    def __str__(self):
        return self.term