from functools import wraps
from django.shortcuts import redirect

def check_user_email_session(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # Check if 'email' is present in the session
        if 'username' not in request.session:
            # Redirect to a login page or another appropriate page
            return redirect('weblogin')  # Change 'login_page' to your actual login page

        # Call the decorated function
        return func(request, *args, **kwargs)

    return wrapper
