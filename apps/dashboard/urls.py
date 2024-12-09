from django.urls import path
from . import views

urlpatterns = [
    path('discere/home/', views.dashboard_home, name='dashboard_home'),
    path('profile/', views.user_settings, name='user_settings'),
    path('library/', views.library, name='library'),
    path('exams/', views.exams_view, name='exams'),
    path("save-exam-set/", views.save_exam_set, name="save_exam_set"),
    path('create-exam/', views.exam_creation, name='exam_creation'),
    
]
