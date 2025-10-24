from django import forms
from .models import Book

class GenreForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['genre']
        # connect form value to current book entry
        widgets = {'book': forms.HiddenInput()}

class StatusForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['status']
        # connect form value to current book entry
        widgets = {'book': forms.HiddenInput()}

class CoverForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['cover_photo']
        # connect form value to current book entry
        widgets = {'book': forms.HiddenInput()}
class BookForm(forms.ModelForm):
    model = Book
    fields = ['title', 'author', 'genre', 'date_started', 'date_ended', 'notes', 'rating', 'status', 'media_type', 'cover_photo']
    widgets = {
        'rating' : forms.RadioSelect,
    }