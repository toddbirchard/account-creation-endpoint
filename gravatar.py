from libgravatar import Gravatar, sanitize_email


def get_gravatar(email):
    """Encrypt email for gravatar id."""
    g = Gravatar(str(email))
    g.get_image()
    return str(g).encode("utf-8")
