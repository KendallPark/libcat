from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from catalog.models import Book, Library

def index(request):
	lastest_book_list = Book.objects.order_by('isbn')[:5]
	template = loader.get_template('catalog/index.html')
	# context dictionary maps template var names to objects
	context = Context({
		'lastest_book_list': lastest_book_list,
		})
	return render(request, 'catalog/index.html', context)

def libpage(request, lib_id):
	return HttpResponse("Library page for %s." % lib_id)

def bookpage(request, book_id):
	book = Book(title="Hello World", owner=Library(name="U-City"), isbn="10120330101")
	return render(request, 'catalog/book.html', {'book': book})

def add_book(request):
	'''try:
		title = request.POST['title']
		author = request.POST['author']
		isbn = request.POST['isbn']
		owner = request.POST['library']
		loan = request.POST['loan']
	except (KeyError, )'''
	return HttpResponse("Book Added")