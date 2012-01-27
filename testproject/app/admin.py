# -*- coding: utf-8 -*-
'''
Created on 27.01.2012

@author: cykooz
'''
from django.contrib import admin

from .models import dynamic_models


admin.site.register(dynamic_models)
