from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'dictionary.views.home'),
    url(r'create-short/$', 'dictionary.views.create_short', name='create_short'),
)