from django.conf.urls import patterns, url
from catalog import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^library/(?P<lib_id>\d+)/$', views.libpage, name='libpage'),
	url(r'^book/(?P<book_id>\d+)/$', views.bookpage, name='bookpage'),
)