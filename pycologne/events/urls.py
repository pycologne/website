from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^details/(?P<pk>\d+)/$', views.view_event, name='events.eventdetails'),
    url(r'^all/$', views.view_events, name='events.allevents'),
)
