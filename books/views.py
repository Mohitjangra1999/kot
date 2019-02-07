
from .models import Book
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic import  View
from .forms import UserForm

class IndexView(ListView):
    queryset = Book.objects.all()
    context_object_name = 'books'
    template_name = 'books/index.html'
   # paginate_by = 2

class DetailView(DetailView):
    model = Book
    template_name = 'books/details.html'

class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'image']
    template_name = 'books/book_creation_form_s.html'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:delete_success')

class Delete_Success_page(TemplateView):
    template_name = 'books/success_delete_page.html'

class UserFormView(View):
    form_class = UserForm
    template_name = 'books/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)     # user is object

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()  # it makes the user to be registered in database of admin but still they are not logined

            #return user object if details are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('books:index')
        else:
            return render(request, self.template_name, {'form': form})



