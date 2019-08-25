from django.conf import settings
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.urls import path

from urllib.parse import urlparse
import string
import random

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

# Task 3. URL shortener
#
# Implement a service to shorten links. Examples of such services:
# http://bit.ly, http://t.co, http://goo.gl
# Link Example: http://bit.ly/1qJYR0y
#
# You will need a template with a form for sending a link (file index.html ),
# and two functions, one for processing GET and POST requests for submitting a URL 
# and displaying the result, and the second for redirecting from a short URL 
# to the original one.
# To store the correspondence of our short keys and full URL, 
# we will use the Django cache, django.core.cache
# The instance cache is already imported, and is used as follows.
# Save value:
#
#  cache.add(key, value)
#
# Extract value:
#
#  cache.get(key, default_value)
#
# The second argument to the get method is the default 
# if the key is not found in the cache.
#
# You can start the server for development and see 
# the answers of your functions in the browser:
#
# python homework03.py runserver


# Configuration, no need to edit
if not settings.configured:
    settings.configure(
        DEBUG=True,
        ROOT_URLCONF=__name__,
        TEMPLATES=[{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['']
        }]
    )


def random_key():
    """
    A random short key made up of numbers and letters.
    The minimum key length is 5 characters. 
    You can use the  library  of random to generate random sequences.
    """
    character = string.ascii_letters + string.digits            # we use thit syntax for generation letters ans numbers
    return ''.join(random.choice(character) for i in range(5))  # we collect all signs together



def index(request):
    """
    When prompted by the GET method, we give an HTML page 
    (index.html template) with a form with one url field of type text 
    (edit the template, complete the form).

    When submitting a form using the POST method, we extract the URL from 
    request.POST and do the following:

    1. Check the URL. The following schemes are allowed: http, https, ftp

    If the URL did not pass the test, display on our page with the form 
    a message about which schemes are supported.

    If the URL passed the check:

    2. Create a random short key consisting of numbers and letters
         (random_key function)

    3. Save URL to cache with generated key:

    cache.add(key, url)

    4. We give the same page with the form and additionally display on 
    it a clickable short link (HTML tag 'a') of the form
    http://localhost:8000/<key>
    """
    key, url = None, None
    cache.add(key, url)

    url = request.POST.get("url")
    err = 'You should use only: http://, https:// or ftp://'

    if url:
        try:
            validate = URLValidator(schemes=('http', 'https', 'ftp',))
            validate(url)
            if cache.get(url):
                key = cache.get(url)
            else:
                key = random_key()
                cache.add(key, url)
            return render(request, 'index.html', {'short_url': 'http://127.0.0.1:8000/' + key})
        except ValidationError:
            return render(request, 'index.html', {'msg': err})
    else:
        return render(request, 'index.html')




def redirect_view(request, key):
    """
    The function processes an abbreviated URL of the form 
    http://localhost:8000/<key> 
    We are looking for a key in the cache (cache.get). 
    If the key is not found, redirect to the main page (/). 
    If found, redirect to the full URL stored under this key.
    """

    link = cache.get(key)

    try:
        return redirect(link)
    except:
        return redirect(to='/')




urlpatterns = [
    path('', index),
    path(r'<key>', redirect_view),
]


if __name__ == '__main__':
    import sys
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)