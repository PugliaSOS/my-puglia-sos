import os
from my_puglia_sos.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    'default':  dj_database_url.config()
    }

# Email settings
EMAIL_HOST = "example@host.com"
EMAIL_PORT = 1234
EMAIL_HOST_USER = 'admin'
EMAIL_HOST_PASSWORD = 'password'
