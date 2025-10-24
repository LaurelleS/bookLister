from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import GenreForm
from .forms import StatusForm
from .forms import BookForm

def home(request):
    recents = Book.objects.order_by('-id')[:5]
    context = {
        'last_books' : recents
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

def deleteBook(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect('allbooks')
    return render(request, 'allbooks.html')

def allbooks(request):
    if request.method == 'GET':
        all = Book.objects.all()
        context = {
            "all" : all
        }
        return render(request, 'allbooks.html', context)

def viewBook(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('allbooks')
    else:
        form = BookForm(instance=book)
        
    context = {
        'form' : form,
    }
    return render(request, 'addbook.html', context)