from django.shortcuts import render

# Create your views here.

# Home page view
def home_view(request):
    return render(request, 'home-page.html')

# Features page view
def feature_view(request):
    return render(request, 'feature-page.html')

# Contact Us page view
def contactus_view(request):
    return render(request, 'contactus-page.html')

# About Us page view
def aboutus_view(request):
    return render(request, 'aboutus-page.html')
