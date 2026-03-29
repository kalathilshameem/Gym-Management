import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gymmgmt.settings')

from gymmgmt.wsgi import application

app = application
