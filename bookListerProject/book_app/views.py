from django.shortcuts import render
from .models import Book
from .forms import GenreForm
from .forms import StatusForm
from .forms import CoverForm

def home(request):
    recents = Book.objects.order_by('-id')[:5]
    context = {
        'last books' : recents
    }
    return render(request, 'home.html', context)

def addBook(request):
    if request.method == 'GET':
        gform = GenreForm()
        sform = StatusForm()
        cform = CoverForm()
        context = {
            gform : 'gform',
            sform : 'sform',
            cform : 'cform',
        }
        return render(request, 'addbook.html', context)
    else:
        title = request.POST.get("title")
        author = request.POST.get("author")
        gform = GenreForm(request.POST)
        rating = int(request.POST.get("rating"))
        sform = StatusForm(request.POST)
        cform = CoverForm(request.POST, request.FILES)

        book = Book(
            title=title,
            author=author,
            rating=rating,
        )
        book.save()
        forms = [gform, sform, cform]
        for form in forms:
            if form.is_valid():
                val = form.save(commit=False)
                val.book = book
                val.save()

        return redirect('allbooks.html')

def allbooks(request):
    context = {
        
    }
    return render(request, 'home.html', context)