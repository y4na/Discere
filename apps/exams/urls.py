from django.urls import path
from . import views

urlpatterns = [
    path('create-exam/', views.exam_creation, name='exam_creation'),
]
