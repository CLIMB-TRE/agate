"""
Settings that are specific to this particular instance of the project.
This can contain sensitive information (such as keys) and should not be shared with others.

REMEMBER: If modfiying the content of this file, reflect the changes in local_settings.example.py
"""

import os
from empty_message_retrieval import EmptyMessageRetrieval

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'u6n(9&8g-3=6d1#jyp^#))you-h&y^-5y7*&hu)cpxzeu_7#j+'

DEBUG = True

ALLOWED_HOSTS = ['*']

ADMIN_EMAIL = 'bear-rsg@contacts.bham.ac.uk'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'django-template.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'django-template_TEST.sqlite3'),
        },
    }
}

ONYX_DOMAIN = ''

MESSAGE_RETRIEVAL = EmptyMessageRetrieval()

LIMITED_PROJECT_LIST = ["synthscape"]
