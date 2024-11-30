from django.shortcuts import render, redirect
from .models import Flashcard
from apps.dashboard.models import StudySet

def flashcard_creation(request):
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation.html', {'study_sets': study_sets})

def flashcard_main(request):
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation-main.html', {'study_sets': study_sets})

def flashcard_viewer(request):
    flashcards = Flashcard.objects.select_related('study_set').all()
    return render(request, 'flashcards/flashcard-viewer.html', {'flashcards': flashcards})

def flashcard_view(request):
    if request.method == 'POST':
        study_set_id = request.POST.get('study_set')
        study_set = StudySet.objects.get(id=study_set_id)

        print(f'Selected StudySet: {study_set}')

        for key in request.POST:
            if key.startswith('term_'):
                term_index = key.split('_')[1]
                definition_key = f'definition_{term_index}'
                term = request.POST.get(key)
                definition = request.POST.get(definition_key)

                print(f'Term: {term}, Definition: {definition}')

                if term and definition:
                    flashcard_set = Flashcard.objects.create(study_set=study_set, term=term, definition=definition)
                    context = {
                        'study_set': flashcard_set.study_set,
                        'term': flashcard_set.term,
                        'definition': flashcard_set.definition,
                    }

        return render(request, 'dashboard/library.html', context)

    return render(request, 'flashcards/flashcard-creation-main.html')

def flashcard_display_view(request):
    flashcards = Flashcard.objects.select_related('study_set').all()  
    return render(request, 'flashcards/flashcard-base.html', {'flashcards': flashcards})

def library_view(request):
    study_sets = StudySet.objects.all()
    return render(request, 'dashboard/library.html', {'study_sets': study_sets})

def flashcard_creation_main(request):
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation-main.html', {'study_sets': study_sets})