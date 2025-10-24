from django.shortcuts import render, redirect
from .models import Book
from .forms import GenreForm
from .forms import StatusForm
from .forms import BookForm

def home(request):
    recents = Book.objects.order_by('-id')[:5]
    context = {
        'last books' : recents
    }
    return render(request, 'home.html', context)

def addBook(request):
    if request.method == 'GET':
        form = BookForm()
        context = {
            'form' : form,
        }
        return render(request, 'addbook.html', context)
    else:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        return redirect('allbooks')

def allbooks(request):
    if request.method == 'GET':
        all = Book.objects.all()
        context = {
            "all" : all
        }
        return render(request, 'home.html', context)