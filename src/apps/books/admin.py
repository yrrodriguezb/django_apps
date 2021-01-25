from django.contrib import admin
from apps.books.models import Author, Book, Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
