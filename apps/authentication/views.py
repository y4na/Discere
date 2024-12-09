from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from apps.dashboard.models import Profile
from django import forms
from django.contrib import messages
# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard_home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

# Signup form
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        }
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }
        help_texts = {
            'username': '',
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.set_password(form.cleaned_data["password"])  # Set the password
            user.save()  # Save the user instance to the database
            
            Profile.objects.create(user=user)

            messages.success(request, 'Your account has been created!')
            return redirect('login')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = SignUpForm()

    return render(request, 'auth/signup.html', {'form': form})




def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/base.html', {'user': request.user})
    else:
        return redirect('login') 

def logout_view(request):
    logout(request)
    return redirect('login')

from django.core.mail import send_mail
import random

verification_codes = {}

def send_verification_code(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            code = random.randint(100000, 999999)  # Generate random 6-digit code
            verification_codes[email] = code
            request.session['email'] = email  # Save email in session for later use

            try:
                send_mail(
                    'Your Password Reset Code',
                    f'Your verification code is: {code}',
                    'noreply@discere.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Verification code sent to your email.')
                return redirect('verify_code')
            except Exception as e:
                messages.error(request, f'Error: {e}')
        else:
            messages.error(request, 'Email is required.')
    return render(request, 'auth/password_reset.html')

def verify_code(request):
    if request.method == 'POST':
        print("POST Data:", request.POST)  # Debugging line
        verification_code = request.POST.get('verification_code')  # Only retrieve the entered code
        email = request.session.get('email')  # Get email from session

        if email and verification_code:
            # Compare the code
            if int(verification_code) == verification_codes.get(email):
                messages.success(request, 'Verification successful!')
                del verification_codes[email]
                del request.session['email']  # Clear session data
                return redirect('update_password', email=email)
            else:
                messages.error(request, 'Invalid verification code. Please try again.')
        else:
            messages.error(request, 'Both email and verification code are required.')

    return render(request, 'auth/verify_code.html')


def update_password(request, email):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if the new passwords match
        if new_password == confirm_password:
            try:
                user = User.objects.get(email=email)  # Find the user by email
                user.set_password(new_password)  # Set the new password
                user.save()
                messages.success(request, 'Your password has been updated successfully.')
                return redirect('login')  # Redirect to login page
            except User.DoesNotExist:
                messages.error(request, 'User not found.')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')

    return render(request, 'auth/reset_password.html', {'email': email})

