from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader
# Create your views here.


def index(request):
    all_books = Book.objects.all()
    template = loader.get_template('books/index.html')
    context = {
        'all_books' : all_books
    }

    return HttpResponse(template.render(context, request))


def detail(request, book_id):
    return HttpResponse("<h2> Details for Book ID : " + str(book_id) + "</h2>")
