from math import ceil
from django import template


register = template.Library()

@register.filter
def partition(value: int, length: int = 3):
    return ceil(value / length)