from django import template
from ..models import Book

register = template.Library()

@register.simple_tag
def total_books():
  return Book.objects.count()