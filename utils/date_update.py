import pandas as pd
import numpy as np
import os, sys, glob
import datetime
import time
start_path = os.getcwd()
proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onspace.settings")
sys.path.append(proj_path)
os.chdir(proj_path)
import django

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from information.models import (
        CompanyCode, EM01, AB09,
        AA06, AA22, AB01, AD01, AZ06
        )