from django.urls import path,include
from django.conf.urls import url
from .import views

urlpatterns = [
        path('', views.index, name='index'),
        url(r'^details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.details),
        path('posts/new', views.new, name='new'),
    ];