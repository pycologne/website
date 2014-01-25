from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='events.details'),
    url(r'^', views.view_events, name='events.all'),
)
