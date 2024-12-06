from django.shortcuts import render


def exam_creation(request):
    return render(request, 'exams/create-exam.html')

# Create your views here.
