from django.urls import path
from . import views

urlpatterns = [
    path('create_exam_card/', views.exam_card_creation, name='create_exam_card'),
    path('exam_card/<int:exam_set_id>/', views.exam_card_viewer, name='exam_card_viewer'),
    path('exam_card_result/', views.exam_card_result_viewer, name='exam_card_result_viewer'),
    path('delete_exam_cards/', views.delete_exam_cards, name='delete_exam_cards'),
    path('update_exam_card_status/', views.update_exam_card_status, name='update_exam_card_status'),
    path('delete_exam_set/<int:exam_set_id>/', views.delete_exam_set, name='delete_exam_set'),
    path('exam_card_view/', views.exam_card_view, name='exam_card_view'),
]
