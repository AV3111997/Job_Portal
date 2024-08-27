from .models import CustomUser

def authenticate(email,password):
    try:
        user = CustomUser.objects.get(email=email)
        if user.check_password(password):
            return user
        else:
            return None
    except CustomUser.DoesNotExist:
        return None