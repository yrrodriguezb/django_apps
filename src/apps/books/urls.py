from django.urls import path
from apps.books.views import (
    AuthorList,
    AuthorDetailView,
    BookList,
    PublisherDetail,
    PublisherList, 
    PublisherBookList
)

app_name = 'books'

urlpatterns = [
    path('', BookList.as_view(), name='books_list'),
    path('authors/', AuthorList.as_view(), name='authors-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('publishers/', PublisherList.as_view(), name='publishers-list'),
    path('publisher/<int:pk>/', PublisherDetail.as_view(), name='publisher-detail'),
    path('publishers/books/<publisher>/', PublisherBookList.as_view(), name='books-publishers'),
]