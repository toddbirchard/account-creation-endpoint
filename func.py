from mailer import welcome_email
from gravatar import get_gravatar
from mailer import welcome_email
from analytics import mixpanel_profile


def subscribe(request):
    """Prepare  a new user account for the subscriber."""
    # Prepare Account Values.
    request_json = request.get_json()
    username = request_json['username']
    email = request_json['email']
    # Derive Gravatar from Email
    grav = get_gravatar(email)
    request_json['gravatar'] = grav
