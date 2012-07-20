import dj_database_url

import os

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': dj_database_url.config(default="postgres://localhost"),
}

SENTRY_KEY = 'XvoJ2ZEubhvB803wU8yL/aDC2EmbjMDFf4oVxGSHbwY3qOKSSeSG0A=='

# Set this to false to require authentication
SENTRY_PUBLIC = False

SENTRY_URL_PREFIX = 'http://mysentry.herokuapp.com/'

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = os.environ.get('PORT', 80)
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    # 'worker_class': 'gevent',
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

