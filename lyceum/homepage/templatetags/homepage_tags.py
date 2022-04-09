from django import template
from string import whitespace
from random import choice

register = template.Library()

@register.filter
def ten_words(value: str):
    k = 0
    for i in range(len(value)):
        if value[i] in whitespace:
            k += 1
        if k >= 10:
            return f'{value[:i]}...'
    return value


@register.simple_tag()
def random_color():
    return choice(('bg-primary', 'bg-success', 'bg-danger', 'bg-warning text-dark', 'bg-info text-dark'))
