from django import forms
from .models import Profile  # or Profile if you're using a separate model

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile  # or Profile
        fields = ['profile_picture']
