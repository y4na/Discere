from django.shortcuts import render, redirect
from .models import Flashcard
from apps.dashboard.models import StudySet

def flashcard_creation(request):
    # Display the form for flashcard creation
    study_sets = StudySet.objects.all()  # Fetch all available study sets
    return render(request, 'flashcards/flashcard-creation.html', {'study_sets': study_sets})

def flashcard_main(request):
    # Display the main page for creating flashcards
    study_sets = StudySet.objects.all()  # Fetch study sets for selection
    return render(request, 'flashcards/flashcard-creation-main.html', {'study_sets': study_sets})

def flashcard_base(request):
    # Base template for flashcards (currently unused)
    return render(request, 'flashcards/flashcard-base.html')

def flashcard_viewer(request):
    # Display flashcards in a viewer
    flashcards = Flashcard.objects.select_related('study_set').all()  # Fetch all flashcards with their study sets
    return render(request, 'flashcards/flashcard-viewer.html', {'flashcards': flashcards})

def flashcard_view(request):
    # Handle the creation of flashcards
    if request.method == 'POST':
        study_set_id = request.POST.get('study_set')  # Get the selected study set ID
        study_set = StudySet.objects.get(id=study_set_id)  # Fetch the study set

        print(f'Selected StudySet: {study_set}')

        for key in request.POST:
            if key.startswith('term_'):
                term_index = key.split('_')[1]
                definition_key = f'definition_{term_index}'
                term = request.POST.get(key)
                definition = request.POST.get(definition_key)

                print(f'Term: {term}, Definition: {definition}')

                if term and definition:
                    Flashcard.objects.create(
                        study_set=study_set,  # Link the flashcard to the selected study set
                        term=term,
                        definition=definition
                    )

        return redirect('flashcard_base')

    return render(request, 'flashcards/flashcard-creation-main.html')

def flashcard_display_view(request):
    # Display all flashcards
    flashcards = Flashcard.objects.select_related('study_set').all()  # Fetch flashcards with related study sets
    return render(request, 'flashcards/flashcard-base.html', {'flashcards': flashcards})

def flashcard_creation_main(request):
    # Display the form for creating flashcards linked to study sets
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation-main.html', {'study_sets': study_sets})
