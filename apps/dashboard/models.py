from django.db import models

class StudySet(models.Model):
    set_name = models.CharField(max_length=255)
    set_subject = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.set_name
    
    def get_id(self):
        return self.id
