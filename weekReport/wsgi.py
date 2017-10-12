# -*- coding: utf-8 -*-
# author: itimor

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weekReport.settings")

application = get_wsgi_application()
