from django.db import models

class StudySet(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)

    def __str__(self):
        return self.name
