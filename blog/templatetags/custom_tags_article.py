from django import template

register = template.Library()


@register.filter(name='get_param')
def get_param(dic, key):
    return dic.get(key)
