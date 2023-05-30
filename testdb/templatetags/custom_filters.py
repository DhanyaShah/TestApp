from django import template

register = template.Library()

@register.filter
def age(array, idx):
    return array[idx-6]

@register.filter
def mul(int, val):
    return int*val

@register.filter
def list(val):
    return range(val)