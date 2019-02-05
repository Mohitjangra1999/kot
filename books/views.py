
from .models import Book
from django.views import generic
from django.views.generic.edit import CreateView

class IndexView(generic.ListView):
    queryset = Book.objects.all()
    context_object_name = 'books'
    template_name = 'books/index.html'
   # paginate_by = 2

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'image']
    template_name = 'books/book_creation_form_s.html'

class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/details.html'


