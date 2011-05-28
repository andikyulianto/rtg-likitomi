import os
import sys
path1 = '/home/patipol/rtg-likitomi'
path2 = '/home/patipol/rtg-likitomi/likitomi'
if path1 not in sys.path:
    sys.path.append(path1)
if path2 not in sys.path:
    sys.path.append(path2)

os.environ['DJANGO_SETTINGS_MODULE'] = 'likitomi.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
