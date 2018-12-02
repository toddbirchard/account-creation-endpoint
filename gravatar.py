import urllib
import hashlib


def get_gravatar(email):
    '''Encrypt email for gravatar id.'''
    email = "someone@somewhere.com"
    default = "https://www.example.com/default.jpg"
    size = 40

    # construct the url
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
    return gravatar_url
