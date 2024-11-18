from django.shortcuts import render

def flashcard_creation(request):
    return render(request, 'flashcards/flashcard-creation.html')
