# -*- coding: utf-8 -*-
'''
Created on 27.01.2012

@author: cykooz
'''
import os
from collections import OrderedDict

from django.db.models import Model, IntegerField, CharField


def create_models_from_config(package):
    import yaml
    from .settings import YAML_PATH

    if not (YAML_PATH and os.path.isfile(YAML_PATH)):
        return

    TYPE_FABRIC_MAP = {
                'int': lambda title: IntegerField(title, default=0),
                'char': lambda title: CharField(title, max_length=255, default=u'')
                }

    models = []

    stream = file(YAML_PATH)
    config = yaml.load(stream)
    stream.close()

    for name, properties in config.iteritems():
        model_members = OrderedDict({
                    '__module__': __name__,
                    'Meta': type('Meta', (), {'verbose_name': properties['title']})
                })

        for field in properties['fields']:
            if field['type'] not in TYPE_FABRIC_MAP:
                raise Exception('Invalid field type - "%s"' % field['type'])

            fabric = TYPE_FABRIC_MAP[field['type']]
            model_members[field['id']] = fabric(field['title'])

        # Create a unique model class name.
        i = 1
        class_name = name
        while class_name in package:
            class_name = '%s%d' % (name, i)
            i += 1

        # Create a model class and add it to the package
        model = type(class_name, (Model,), model_members)
        package[class_name] = model
        models.append(model)

    return models


# This should be at the end of the file
dynamic_models = create_models_from_config(locals())
