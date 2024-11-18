from django.shortcuts import render
from .models import FlashcardSet, Flashcard

def flashcard_creation(request):
    return render(request, 'flashcards/flashcard-creation.html')

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
        
        return redirect('flashcard_display') 

    return render(request, 'flashcard/flashcard-creation-page.html')

def flashcard_display_view(request):
    flashcards = Flashcard.objects.all()
    return render(request, 'flashcard/flashcard-display-page.html', {'flashcards': flashcards})

