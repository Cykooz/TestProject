# -*- coding: utf-8 -*-
'''
Created on 27.01.2012

@author: cykooz
'''
import os

from django.conf import settings


YAML_PATH = getattr(settings, 'YAML_PATH', os.path.join(os.path.dirname(__file__), 'config.yaml'))

