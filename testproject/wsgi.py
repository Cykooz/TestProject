# -*- coding: utf-8 -*-
'''
Created on 19.12.2011

@author: cykooz
'''
import sys

from django.core import management


def application_factory(global_conf, settings):
    try:
        mod = __import__(settings)
        components = settings.split('.')
        for comp in components[1:]:
            mod = getattr(mod, comp)

    except ImportError, e:
        sys.stderr.write("Error loading the settings module '%s': %s"
        % (settings, e))
        sys.exit(1)

    # Setup settings
    management.setup_environ(mod)

    from django.core.handlers.wsgi import WSGIHandler

    # Run WSGI handler for the application
    return WSGIHandler()