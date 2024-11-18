from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/', views.user_settings, name='user_settings'),
    path('library/', views.library, name='library'),
    path('exams/', views.exams_view, name='exams'),
]
