from django import forms
from .models import ExamSet, Question

class ExamSetForm(forms.ModelForm):
    class Meta:
        model = ExamSet
        fields = ['name', 'subject']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'answer_text']