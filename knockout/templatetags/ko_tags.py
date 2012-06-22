# -*- coding: utf-8 -*-

from django import template
from django.db.models.loading import get_model

register = template.Library()

@register.inclusion_tag('knockout/model.js')
def ko_model(app_model):
    model = get_model(*app_model.split('.'))
    return {
        'model_name':model.__name__,
        'fields':model._meta.fields
    }


@register.inclusion_tag('knockout/viewmodel.js')
def ko_view_model(app_model,verbose_name_plural=None):
    model = get_model(*app_model.split('.'))
    if verbose_name_plural is None:
        verbose_name_plural = "%ss" % model.__name__

    return {
        'model_name': model.__name__,
        'verbose_name_plural':verbose_name_plural
    }

