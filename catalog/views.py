from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from catalog.models import Book, Library, BookForm, LibraryForm

def index(request):
    lastest_book_list = Book.objects.order_by('isbn')[:5]
    template = loader.get_template('catalog/index.html')
    # context dictionary maps template var names to objects
    context = Context({
        'lastest_book_list': lastest_book_list,
        })
    return render(request, 'catalog/index.html', context)

def libpage(request, lib_id):
    try: 
        library = Library.objects.get(id=lib_id)
    except Library.DoesNotExist:
        raise Http404
    try:
        topbook = Book.objects.filter(owner=library).order_by('hits')[::-1][0]
    except IndexError:
        topbook = None
    except Book.DoesNotExist:
        raise Http404
    return render(request, 'catalog/library.html', {'library':library, 'topbook':topbook})

def bookpage(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.hits += 1 # updates popularity based on web hits
        book.save()
    except Book.DoesNotExist:
        raise Http404
    return render(request, 'catalog/book.html', {'book':book})

def add_book(request):
    bookform = BookForm()
    return render(request, 'catalog/add_book.html', {'bookform':bookform})

def add_library(request):
    libform = LibraryForm()
    return render(request, 'catalog/add_library.html', {'libform':libform})

def submit_book(request):
    try:
        f = BookForm(request.POST)
        book = f.save()
    except ValueError:
        bookform = BookForm()
        return render(request, 'catalog/add_book.html', {'bookform':bookform, 'err': "Missing Field Data",})
    else:
        return render(request, 'catalog/book_submit.html', {'book':book,})

def submit_library(request):
    try:
        f = LibraryForm(request.POST)
        library = f.save()
    except ValueError:
        libform = LibraryForm()
        return render(request, 'catalog/add_library.html', {'libform':libform, 'err': "Missing Field Data",})
    else:
        return render(request, 'catalog/library_submit.html', {'library':library,})

def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
    else:
        return HttpResponse("No query")
    try:
        books = Book.objects.filter(title__contains=q)
        print books
        if not books: # checks if there are no title results
            try:
                books = Book.objects.all().filter(isbn=q)
            except ValueError:
                pass
    except Book.DoesNotExist:
        raise Http404
    return render(request, 'catalog/search_results.html', {'q':q, 'books':books,})