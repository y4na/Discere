from django.urls import path
from . import views
from .views import send_message

urlpatterns = [
    path('', views.home_view, name='home'),
    path('feature/', views.feature_view, name='feature'), 
    path('contact-us/', views.contactus_view, name='contactus'),
    path('about-us/', views.aboutus_view, name='aboutus'),
    path('send_message/', send_message, name='send_message'),
]
