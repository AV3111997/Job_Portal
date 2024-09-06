from .models import User
from django.core.mail import send_mail
from django.conf import settings
import secrets


#sent the otp to the email of user
def send_otp_email(email, otp):
    subject = 'Your OTP for Login'
    message = f'Your OTP is: {otp}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    print(otp,email)
    send_mail(subject, message, from_email, recipient_list)

#sent the otp to the email of user
def send_password_reset_email(email, link):
    subject = 'link to reset password in JobPortal'
    message = f'link:{link}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)



def generate_token(length=20):
    """Generate a random token."""
    return secrets.token_urlsafe(length)

def authenticate(email,password):
    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return user
        else:
            return None
    except User.DoesNotExist:
        return None