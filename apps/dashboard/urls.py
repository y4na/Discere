from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.user_settings, name='user_settings'),
    path('library/', views.library, name='library'),
]