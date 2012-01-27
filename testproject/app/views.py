# -*- coding: utf-8 -*-
'''
Created on 27.01.2012

@author: cykooz
'''
from django import http
from django.db.models.loading import get_app, get_model, get_models
from django.views.generic.base import TemplateView, View
from django.utils import simplejson as json


class JSONResponseMixin(object):
    def render_to_response(self, context):
        "Returns a JSON response containing 'context' as payload"
        return self.get_json_response(self.convert_context_to_json(context))

    def get_json_response(self, content, **httpresponse_kwargs):
        "Construct an `HttpResponse` object."
        return http.HttpResponse(content,
            content_type='application/json',
            **httpresponse_kwargs)

    def convert_context_to_json(self, context):
        "Convert the context dictionary into a JSON object"
        return json.dumps(context)


class Index(TemplateView):
    template_name = 'index.html'


class ModelsList(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        app = get_app('app')
        models = [{'name': model.__name__, 'title': model._meta.verbose_name}
                  for model in get_models(app)
                  if not model._meta.abstract
                 ]
        return self.render_to_response(models)


class ModelData(JSONResponseMixin, View):

    def get(self, request, *args, **kwargs):
        model_name = request.GET.get('model_name', '')
        model = get_model('app', model_name)
        objects = model.objects.all()
        results = {}
        results['titles'] = [field.verbose_name
                             for field in model._meta.fields
                             if not field.primary_key
                            ]
        results['rows'] = [
                            [
                                field.value_to_string(obj)
                                for field in model._meta.fields
                                if not field.primary_key
                            ]
                            for obj in objects
                          ]
        return self.render_to_response(results)


