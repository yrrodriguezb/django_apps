from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from apps.books.models import Author, Book, Publisher


class PublisherList(ListView):
    model = Publisher
    context_object_name = 'publishers'

class PublisherDetail(DetailView):
    context_object_name = 'publisher'
    queryset = Publisher.objects.all()

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

class BookList(ListView):
    queryset = Book.objects.order_by('-publication_date')
    context_object_name = 'books_list'

class AcmeBookList(ListView):
    context_object_name = 'acme_book_list'
    queryset = Book.objects.filter(publisher__name='ACME Publishing')
    template_name = 'books/acme_book_list.html'

class PublisherBookList(ListView):
    context_object_name = 'books_list'
    template_name = 'books/books_by_publisher.html'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)


class AuthorList(ListView):
    queryset = Author.objects.all()
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    context_object_name = 'author'
    queryset = Author.objects.all()

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj