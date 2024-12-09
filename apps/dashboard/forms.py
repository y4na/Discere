from django import forms
from .models import Profile
from django.contrib.auth.models import User

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']


class CustomPasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput, label="Current Password")
    new_password = forms.CharField(widget=forms.PasswordInput, label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm New Password")
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")
        
        # Check if new password and confirm password match
        if new_password != confirm_password:
            raise forms.ValidationError("New password and confirmation do not match.")
        
        # Check if current password is correct
        current_password = cleaned_data.get("current_password")
        if not self.user.check_password(current_password):
            raise forms.ValidationError("The current password is incorrect.")
        
        return cleaned_data
    
