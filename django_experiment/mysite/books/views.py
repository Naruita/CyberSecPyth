from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Book
from django.template import loader


def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {
        'all_books' : all_books
    }
    return render(request, 'books/index.html', context)


def detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404('Hey, I don\'t think that exists?')
    return render(request, 'books/detail.html', {'book': book})
