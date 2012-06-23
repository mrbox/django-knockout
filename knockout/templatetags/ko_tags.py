# -*- coding: utf-8 -*-

from django import template
from django.db.models.loading import get_model

register = template.Library()

@register.inclusion_tag('knockout/model.js',takes_context=True)
def ko_model(context,app_model,context_variable_name="ko_model"):
    model = get_model(*app_model.split('.'))
    context[context_variable_name] = model.__name__
    return {
        'model_name':model.__name__,
        'fields':model._meta.fields
    }


@register.inclusion_tag('knockout/viewmodel.js',takes_context=True)
def ko_view_model(context,app_model,verbose_name_plural=None,context_varialbe_name="ko_view_model"):
    model = get_model(*app_model.split('.'))
    if verbose_name_plural is None:
        verbose_name_plural = "%ss" % model.__name__
    view_model_name = "%sListViewName" % model.__name__
    context[context_varialbe_name] = view_model_name
    return {
        'view_model_name': view_model_name,
        'verbose_name_plural':verbose_name_plural
    }

