from django.db import models
from django.forms import ModelForm
from django.contrib import admin

class Library(models.Model):
    name = models.CharField(max_length=200, verbose_name='Library Name')
    def __unicode__(self):
        return unicode(self.name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField(verbose_name='ISBN')
    owner = models.ForeignKey(Library)
    loan = models.BooleanField(default=True, verbose_name='Available for Interlibrary Loan?')
    hits = models.IntegerField(default=0)
    def __unicode__(self):
        return unicode(self.title)

class LibraryForm(ModelForm):
    class Meta:
        model = Library

class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('hits',)

# for testing
class LibraryAdmin(admin.ModelAdmin):
    list_display = ["name"]

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "isbn", "owner", "loan", "hits"]

admin.site.register(Book, BookAdmin)
admin.site.register(Library, LibraryAdmin)
