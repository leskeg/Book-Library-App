from django.conf.urls import patterns, include, url
from myapp.myapi import *

book_resource = BookResource()
publisher_resource = PublisherResource()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^books/', include(book_resource.urls)),
    url(r'^publishers/', include(publisher_resource.urls)),

    url(r'^addbook/$', 'myapp.views.addBook'),
    url(r'^editbook/$', 'myapp.views.editBook'),
    url(r'^deletebook/$', 'myapp.views.deleteBook'),

    url(r'^admin/', include(admin.site.urls)),
)