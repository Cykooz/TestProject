# -*- coding: utf-8 -*-
'''
Created on 27.01.2012

@author: cykooz
'''
from django.conf.urls.defaults import patterns, url

from .views import Index, ModelsList, ModelData

urlpatterns = patterns('',
    url(r'^$', Index.as_view(), name='app-index'),
    url(r'^models$', ModelsList.as_view(), name='app-get_models'),
    url(r'^model_data$', ModelData.as_view(), name='app-get_model_data'),
)
