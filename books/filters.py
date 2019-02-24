from django.contrib.auth.models import User
import django_filters
from .models import Book

class UserFilter(django_filters.FilterSet):

    class Meta:
        model = User
        fields = ['username', 'email', ]

class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Book
        fields = ['name', ]