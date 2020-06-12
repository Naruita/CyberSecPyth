from django.views import generic
from .models import Book
from django.views.generic.edit import CreateView


class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'
