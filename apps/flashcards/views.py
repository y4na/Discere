from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from apps.dashboard.models import StudySet

def flashcard_creation(request):
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation.html', {
        'study_sets': study_sets,
        'study_set': study_sets.first() if study_sets.exists() else None
    })

def flashcard_viewer(request):
    flashcards = Flashcard.objects.select_related('study_set').all()
    return render(request, 'flashcards/flashcard-viewer.html', {'flashcards': flashcards})

def flashcard_view(request):
    if request.method == 'POST':
        study_set_id = request.POST.get('study_set')

        if not study_set_id or not study_set_id.isdigit():
            return render(request, 'flashcards/flashcard-creation.html', {
                'error': "Invalid or missing study set ID.",
                'study_sets': StudySet.objects.all()
            })

        study_set = get_object_or_404(StudySet, id=int(study_set_id))

        flashcard_count = 0

        for key in request.POST:
            if key.startswith('term_'):
                term_index = key.split('_')[1]
                definition_key = f'definition_{term_index}'
                term = request.POST.get(key)
                definition = request.POST.get(definition_key)

                if term and definition:
                    Flashcard.objects.create(
                        study_set=study_set,
                        term=term,
                        definition=definition
                    )
                    flashcard_count += 1

        study_set.flashcard_count += flashcard_count
        study_set.save()

        return redirect('library_view')

    return render(request, 'flashcards/flashcard-creation.html')

def flashcard_display_view(request):
    flashcards = Flashcard.objects.select_related('study_set').all()  
    return render(request, 'flashcards/flashcard-base.html', {'flashcards': flashcards})

def library_view(request):
    study_sets = StudySet.objects.all()
    return render(request, 'dashboard/library.html', {'study_sets': study_sets})