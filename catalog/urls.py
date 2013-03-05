from django.conf.urls import patterns, url
from catalog import views

urlpatterns = patterns('', 
    url(r'^$', views.index, name='index'),
    url(r'^library/(?P<lib_id>\d+)/$', views.libpage, name='libpage'),
    url(r'^book/(?P<book_id>\d+)/$', views.bookpage, name='bookpage'),
    url(r'^add/book/$', views.add_book, name='add_book'),
    url(r'^add/library/$', views.add_library, name='add_library'),
    url(r'^add/book/submit/$', views.submit_book, name='submit_book'),
    url(r'^add/library/submit/$', views.submit_library, name='submit_library'),
)