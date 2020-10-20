"""
WSGI config for techniqo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

#import os
import os, sys

# add the hellodjango project path into the sys.path
sys.path.append('/var/www/techniqo/techniqo/')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/var/www/techniqo/venv/Lib/site-packages')

# poiting to the project settings
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hellodjango.settings")
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techniqo.settings')

application = get_wsgi_application()
