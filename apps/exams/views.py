import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import ExamCard
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.dashboard.models import ExamSet

def exam_card_creation(request):
    exam_sets = ExamSet.objects.all()
    return render(request, 'exams/exam-card-creation.html', {
        'exam_sets': exam_sets,
        'exam_set': exam_sets.first() if exam_sets.exists() else None
    })

def exam_card_viewer(request, exam_set_id):
    # Convert exam_set_id to integer and validate
    try:
        exam_set_id = int(exam_set_id)
    except (ValueError, TypeError):
        return redirect('library')  # Or handle the error appropriately

    exam_cards = ExamCard.objects.filter(exam_set_id=exam_set_id)
    exam_set = get_object_or_404(ExamSet, id=exam_set_id)
    return render(request, 'exams/exam-card-viewer.html', {
        'exam_cards': exam_cards, 
        'exam_set': exam_set
    })

def exam_card_result_viewer(request):
    exam_cards = ExamCard.objects.all()
    return render(request, 'exams/exam-result.html', {'exam_cards': exam_cards})

def exam_card_view(request):
    if request.method == 'POST':
        exam_set_id = request.POST.get('exam_set')

        if not exam_set_id or not exam_set_id.isdigit():
            return render(request, 'exams/exam-creation.html', {
                'error': "Invalid or missing exam set ID.",
                'exam_sets': ExamSet.objects.all()
            })

        exam_set = get_object_or_404(ExamSet, id=int(exam_set_id))

        exam_card_count = 0
        # Iterating through the form's POST data
        for key in request.POST:
            if key.startswith('term_'):
                term_index = key.split('_')[1]
                definition_key = f'definition_{term_index}'
                term = request.POST.get(key)
                definition = request.POST.get(definition_key)

                if term and definition:
                    ExamCard.objects.create(
                        exam_set=exam_set,
                        term=term,
                        definition=definition
                    )
                    exam_card_count += 1

        # Update the exam set with the new card count
        exam_set.exam_card_count += exam_card_count
        exam_set.save()

        return redirect('library_view')  # Or another URL you want to redirect to after submission

def library_view(request):
    exam_sets = ExamSet.objects.all()
    return render(request, 'dashboard/library.html', {'exam_sets': exam_sets})

@csrf_exempt
def delete_exam_cards(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            exam_set_id = data.get('exam_set_id')

            if not exam_set_id:
                return JsonResponse({'success': False, 'message': 'Exam set ID is missing.'}, status=400)

            exam_set = get_object_or_404(ExamSet, id=exam_set_id)
            ExamCard.objects.filter(exam_set=exam_set).delete()
            exam_set.delete()

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)

def update_exam_card_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        exam_card_id = data.get('exam_card_id')
        status_key = data.get('status_key')
        status_value = data.get('status_value')

        exam_card = ExamCard.objects.get(id=exam_card_id)

        if status_key == 'isNotSure':
            exam_card.isNotSure = status_value
        elif status_key == 'isGotIt':
            exam_card.isGotIt = status_value

        exam_card.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False}, status=400)

def delete_exam_set(request, exam_set_id):
    exam_set = get_object_or_404(ExamSet, id=exam_set_id)

    if request.method == 'POST':
        exam_set.delete()
        return redirect('library')

    return render(request, 'exams/confirm_delete.html', {'exam_set': exam_set})
