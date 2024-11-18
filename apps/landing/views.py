from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage

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

# Sending email feeback from user
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse

def send_message(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')  # User's email address
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Combine first and last names for sender's name
        sender_name = f"{first_name} {last_name}"

        # Email content for the admin/recipient
        admin_subject = f"Contact Form Submission: {subject}"
        admin_body = f"""
        You have received a new message from {sender_name} ({email}).

        Subject: {subject}

        Message:
        {message}
        """

        # Email content for the auto-reply
        reply_subject = "We Received Your Message!"
        reply_body = f"""
        Hi {first_name},

        Thank you for contacting us! We have received your message and will get back to you shortly.

        Here’s a copy of your message:
        Subject: {subject}
        Message:
        {message}

        Best regards,
        The Discere Support Team
        """

        # Default email nga sendan sa email (might create an email for this soon)
        admin_email = 'brix.bitayo@gmail.com'

        try:
            # Send the email to admin email
            admin_email_message = EmailMessage(
                subject=admin_subject,
                body=admin_body,
                from_email=email, 
                to=[admin_email], 
            )
            admin_email_message.send()

            # Send the auto-reply
            reply_email_message = EmailMessage(
                subject=reply_subject,
                body=reply_body,
                from_email='brix.bitayo@gmail.com',  # admin email ni siya ari para sa reply
                to=[email],  # User's email as the recipient
            )
            reply_email_message.send()

            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")

    return redirect('contactus')