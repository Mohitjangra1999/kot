
from .models import Book
from django.views import generic
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    template_name = 'books/index.html'

    def get_queryset(self):
        return Book.objects.all()

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'image']

class DetailView(generic.DetailView):
    template_name = 'books/details.html'
    model = Book

