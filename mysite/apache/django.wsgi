import os, sys
sys.path.append('C:/Users/Patipol/rtg-likitomi')

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
