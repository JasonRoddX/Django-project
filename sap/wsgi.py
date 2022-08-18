"""
WSGI config for sap project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

## Necesario con ambos casos.
sys.path.insert(0, "/home/sistemas/Django/personas_django/sap")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sap.settings')

application = get_wsgi_application()
