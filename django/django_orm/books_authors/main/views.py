from django.shortcuts import render, HttpResponse, redirect

from .models import Author, Book

# Create your views here.
def index(request):
    context = {
        'all_authors' : Author.objects.all(),
        'all_books' : Book.objects.all()
    }
    return render(request, "index.html", context)

def addingBook(request):
    Book.objects.create(
        title = request.POST['titleLabel'],
        desc = request.POST['descLabel']
    )

    return redirect('/')

def bookView(request, id):
    context = {
        'this_book': Book.objects.get(id=id),
        'all_authors': Author.objects.all()
    }

    return render(request, "book_info.html", context)


def authorToBook(request, id2):
    selected_book = Book.objects.get(id=id2)  
    selected_author = Author.objects.get(id=request.POST['authorSelect'])   
    
    selected_book.authors.add(selected_author)


    return redirect(request.META.get('HTTP_REFERER'))


def addAuthor(request):
    context = {
        'all_authors': Author.objects.all(),
        'all_books': Book.objects.all()
    }
    return render(request, "authors.html", context)

def realAddAuthor(request):
    Author.objects.create(
        first_name = request.POST['firstNameLabel'],
        last_name = request.POST['lastNameLabel'],
        notes = request.POST['notesLabel']
    )

    return redirect(request.META.get('HTTP_REFERER'))

def showAuthor(request, id3):
    context = {
        'this_author': Author.objects.get(id=id3),
        'all_books': Book.objects.all()
    }
    return render(request, "author_info.html", context)


def bookToAuthor(request, id4):
    selected_author = Author.objects.get(id=id4)  
    selected_book = Book.objects.get(id=request.POST['bookSelect'])   
    
    selected_book.authors.add(selected_author)


    return redirect(request.META.get('HTTP_REFERER'))