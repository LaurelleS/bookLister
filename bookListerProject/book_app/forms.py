from django import forms
from .models import Book

class GenreForm:
    class Meta:
        model = Book
        fields = ['genre']

class StatusForm:
    class Meta:
        model = Book
        fields = ['status']