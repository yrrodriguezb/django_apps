from django.urls import path
from apps.books.views import (
    AuthorList,
    AuthorDetailView,
    BookList,
    DjangoBookList,
    PublisherUpdateView,
    PublisherDetail,
    PublisherList, 
    PublisherBookList
)

app_name = 'books'

urlpatterns = [
    path('', BookList.as_view(), name='books-list'),
    path('authors/', AuthorList.as_view(), name='authors-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('publishers/', PublisherList.as_view(), name='publishers-list'),
    path('publisher/<int:pk>/detail', PublisherDetail.as_view(), name='publisher-detail'),
    path('publisher/<int:pk>/edit', PublisherUpdateView.as_view(), name='publisher-edit'),
    path('publishers/books/<publisher>/', PublisherBookList.as_view(), name='book-publishers'),
    path('django/', DjangoBookList.as_view(), name='django-books'),
]