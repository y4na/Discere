from django.shortcuts import render
from .models import FlashcardSet, Flashcard
from apps.dashboard.models import StudySet

def flashcard_creation(request):
    # ma display idk
    return render(request, 'flashcards/flashcard-creation.html')

def flashcard_main(request):
    # actual creation happens here
    return render(request, 'flashcards/flashcard-creation-main.html')

def flashcard_base(request):
    # no use
    return render(request, 'flashcard-base.html')

def flashcard_viewer(request):
    return render(request, 'flashcards/flashcard-viewer.html')

def flashcard_view(request):
    if request.method == 'POST':
        set_name = request.POST.get('set_name')
        flashcard_set = FlashcardSet.objects.create(name=set_name)
        
        print(f'Created FlashcardSet: {flashcard_set}')

        for key in request.POST:
            if key.startswith('term_'):
                term_index = key.split('_')[1]
                definition_key = f'definition_{term_index}'
                term = request.POST.get(key)
                definition = request.POST.get(definition_key)

                print(f'Term: {term}, Definition: {definition}')

                if term and definition:
                    Flashcard.objects.create(
                        flashcard_set=flashcard_set,
                        term=term,
                        definition=definition
                    )
        
        return redirect('flashcard_base') 

    return render(request, 'flashcard/templates/flashcard-creation-main.html')

def flashcard_display_view(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcards/templates/flashcard-base.html', {'flashcards': flashcards})

def flashcard_creation_main(request):
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation-main.html', {'study_sets': study_sets})



