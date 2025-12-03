"""
WSGI config for athletitrack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the Python path
#path = '/home/antonio19/athletitrack'  # <-- change this to your PythonAnywhere project folder
#if path not in sys.path:
    #sys.path.append(path)

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'athletitrack.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
    