from mailer import welcome_email
from gravatar import get_gravatar
from mailer import welcome_email
from analytics import mixpanel_profile
from db import UserAccounts


def subscribe(req):
    """Prepare  a new user account for the subscriber."""
    # Prepare Account Values.
    req_json = req.get_json()
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    username = req.form.username
    email = req.form.email
    grav = get_gravatar(email)   # Derive Gravatar from Email
    # Insert DB record
    new_account = UserAccounts(username, email, grav)
    new_account.create_account
    # Welcome via Email
    welcome_email(email)

    return 'Hello {}!'.format(email)
