from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^titles/$', views.titles_menu, name='titles'),
    url(r'^(?P<spoiler_id>[0-9]+)/$', views.spoiler_detail, name='detail'),
]
