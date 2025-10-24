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
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'date_started', 'date_ended', 'notes', 'rating', 'status', 'media_type', 'cover_photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'media_type': forms.Select(attrs={'class': 'form-select'}),
            'cover_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'date_started': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_ended': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'rating': forms.RadioSelect,  # will override in template
        }