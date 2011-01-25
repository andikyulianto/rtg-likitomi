import os, sys
sys.path.append('/home/patipol/rtg-likitomi')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
