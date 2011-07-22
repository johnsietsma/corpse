import os
import sys

app_path = os.path.dirname(os.path.realpath(__file__))
app_dir = os.path.split(app_path)[0]

sys.path.append(app_path)
sys.path.append(app_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'corpse.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
