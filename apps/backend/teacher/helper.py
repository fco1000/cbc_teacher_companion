from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from ctc.settings import EMAIL_HOST_USER as sender_email
from .models import Position,User,School
from django.template.loader import render_to_string
import secrets

# Helper function to check if a user is the headmaster or deputy
def is_headmaster_or_deputy(user):
    # Implement your logic here to check group membership or any other criteria
    return user.groups.filter(name__in=["headmaster", "deputy"]).exists()

# Helper function to check if a user is an admin
def is_admin(user):
    # Implement your logic here to check group membership or any other criteria
    return user.groups.filter(name="admin").exists()

# Helper function to send an activation email
def send_account_email(email, password):
    subject = 'Activate Your Account'
    email_content = render_to_string('teachers/new_user_email.html',{'email':email,'password':password})
    from_email = sender_email  # Change this to your email address
    recipient_list = [email]
    send_mail(
        subject, 
        from_email, 
        recipient_list, 
        fail_silently=False,
        html_message=email_content, 
    )
    
def generate_random_password():
    length = 9
    password = "".join(secrets.choice("abcdefghijklmnopqrstuvwxzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+?/") for i in range(length))
    return password
    

    
        