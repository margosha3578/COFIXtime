from django import template

register = template.Library()


@register.filter
def split(value, delimiter):
    if value is not None and 'set' not in value:
        symbols_to_remove = ["{", "'", "}"]
        for symbol in symbols_to_remove:
            value = value.replace(symbol, '')
        return list(value.split(delimiter))
    else:
        return '-'

