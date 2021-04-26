import os
from .base import *

DEBUG = False
SECRET_KEY = 'f&tqup#v&qw94r&!ubsnf4de+6n&s2kjo#=86p1@%^zaz@_w_-'
ALLOWED_HOSTS = ['localhost', 'rocketman.learnwagtail.com', '*']

cwd = os.getcwd()
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": f"{cwd}/.cache",
    }
}

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql_psycopgq2',
        "NAME": 'rocketman',
        "USER": 'rocketman',
        "PASSWORD": 'd(=W:u6C9gZ;.tq',
        "HOST": 'localhost',
        "PORT"; "",
    }
}

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://1a6ba3b1acc64d8a9aa483716a191455@o580764.ingest.sentry.io/5735649",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

try:
    from .local import *
except ImportError:
    pass
