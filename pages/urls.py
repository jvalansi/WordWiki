from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<word>\w+)/$', views.text, name='text'),
    url(r'^(?P<word>\w+)/update$', views.text, name='text'),
    url(r'^(?P<word>\w+)/create$', views.text, name='text'),
)