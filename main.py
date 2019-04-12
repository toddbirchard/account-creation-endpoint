import flask
from gravatar import get_gravatar
from mailer import welcome_email
from analytics import mixpanel_profile
from db import UserAccounts


def subscribe(req):
    """Prepare  a new user account for the subscriber."""
    # Prepare Account Values.
    req_json = req.get_json()
    username = req.form['username']
    email = req.form['email']
    grav = get_gravatar(email)   # Derive Gravatar from Email
    # Insert DB record
    new_account = UserAccounts(username, email, grav)
    new_account.create_account
    # Welcome via Email
    welcome_email(email)

    return new_account.create_account
