from django.shortcuts import render
from .models import Book
from .forms import BookForm

def home(request):
    recents = Book.objects.order_by('-id')[:5]
    context = {
        'last books' : recents
    }
    return render(request, 'home.html', context)

def addBook(request):
    gform = GenreForm()
    sform = StatusForm()
    context = {
        gform : 'gform'
        sform : 'sform'
    }
    return render(request, 'home.html', context)

def allbooks(request):
    context = {
        
    }
    return render(request, 'home.html', context)