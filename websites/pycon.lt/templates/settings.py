from pyconlt.settings.base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pycon',
        'USER': 'pycon',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

SECRET_KEY = '{{ secrets.django.secret_key }}'

ALLOWED_HOSTS = [
    'pycon.lt',
    'www.pycon.lt',
]
