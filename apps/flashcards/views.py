import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.dashboard.models import StudySet

def flashcard_creation(request):
    study_sets = StudySet.objects.all()
    return render(request, 'flashcards/flashcard-creation.html', {
        'study_sets': study_sets,
        'study_set': study_sets.first() if study_sets.exists() else None
    })

def flashcard_viewer(request, study_set_id):
    if request.method == 'POST':
        return redirect('flashcard-viewer', study_set_id=study_set_id)

    flashcards = Flashcard.objects.filter(study_set_id=study_set_id)
    return render(request, 'flashcards/flashcard-viewer.html', {'flashcards': flashcards})

def flashcard_editor(request, study_set_id):
    study_set = get_object_or_404(StudySet, id=study_set_id)
    
    if request.method == 'POST':
        return redirect('flashcard-editor', study_set_id=study_set_id)
    
    flashcards = Flashcard.objects.filter(study_set_id=study_set_id)
    
    return render(request, 'flashcards/flashcard-edit.html', {
        'study_set': study_set,
        'flashcards': flashcards
    })

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

def library_view(request):
    study_sets = StudySet.objects.all()
    return render(request, 'dashboard/library.html', {'study_sets': study_sets})

@csrf_exempt
def delete_flashcards(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            study_set_id = data.get('study_set_id')

            if not study_set_id:
                return JsonResponse({'success': False, 'message': 'Study set ID is missing.'}, status=400)

            study_set = get_object_or_404(StudySet, id=study_set_id)
            Flashcard.objects.filter(study_set=study_set).delete()
            study_set.delete()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

def delete_study_set(request, study_set_id):
    if request.method == "DELETE":
        study_set = get_object_or_404(StudySet, id=study_set_id)
        study_set.delete()
        return JsonResponse({"message": "Study set deleted successfully"}, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=400)

def update_flashcards(request, study_set_id):
    study_set = get_object_or_404(StudySet, id=study_set_id)
    flashcards = Flashcard.objects.filter(study_set_id=study_set_id)

    if request.method == 'POST':
        flashcard_count = 0
        for key in request.POST:
            if key.startswith('term_'):
                term_index = key.split('_')[1]
                definition_key = f'definition_{term_index}'
                term = request.POST.get(key)
                definition = request.POST.get(definition_key)

                if term and definition:
                    # Check if flashcard exists
                    flashcard = Flashcard.objects.filter(study_set=study_set, term=term).first()

                    if flashcard:
                        flashcard.definition = definition
                        flashcard.save()
                    else:
                        # If no existing flashcard found, create a new one
                        Flashcard.objects.create(
                            study_set=study_set,
                            term=term,
                            definition=definition
                        )
                    flashcard_count += 1

        study_set.flashcard_count = flashcard_count
        study_set.save()

        return redirect('flashcard_viewer', study_set_id=study_set_id)

    return render(request, 'flashcards/flashcard-edit.html', {
        'flashcards': flashcards,
        'study_set': study_set
    })
