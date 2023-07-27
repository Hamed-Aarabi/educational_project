from django import template

register = template.Library()


@register.filter
def digit_seperator(value):
    value = str(value)
    if len(value) <= 3:
        return value
    else:
        return value[:-3] + ',' + value[-3:]
