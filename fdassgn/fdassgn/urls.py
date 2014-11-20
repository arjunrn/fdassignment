from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'dictionary.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<r_word>[a-zA-Z0-9]+)/$', 'dictionary.views.redirection', name='redirection'),
)
