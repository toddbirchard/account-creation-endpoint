from libgravatar import Gravatar


def get_gravatar(email):
    '''Encrypt email for gravatar id.'''

    g = Gravatar(email)
    g.get_image()
    return g
