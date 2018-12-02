import urllib
import hashlib

# Set your variables here
email = "someone@somewhere.com"
default = "https://www.example.com/default.jpg"
size = 40

# construct the url
gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
