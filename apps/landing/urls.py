from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('feature/', views.feature_view, name='feature'), 
    path('contact-us/', views.contactus_view, name='contactus'),
    path('about-us/', views.aboutus_view, name='aboutus'),
]
