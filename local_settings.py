import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'jrsmith072@gmail.com'
EMAIL_HOST_PASSWORD = 'Mookie09'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
