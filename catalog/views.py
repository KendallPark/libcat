from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from catalog.models import Book, Library, BookForm

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
    f = BookForm(request.POST)
    new_book = f.save()
    return HttpResponse("Book Added")