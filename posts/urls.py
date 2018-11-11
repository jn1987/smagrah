from django.urls import path,include
from django.conf.urls import url
from .import views

urlpatterns = [
        path('', views.index, name='index'),
        url(r'^details/(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.details),
        path('posts/new', views.new, name='new'),
        path('login/posts/new', views.new, name='new'),
        path('search/', views.search, name='search'),
        path('search/search', views.search, name='search'),
        path('signup/', views.signup, name='signup'),
        path('posts/signup/', views.signup, name='signup'),
        path('login/', views.login_view, name='login'),
        path('posts/login/', views.login_view, name='login'),
        path('logout/', views.logout_view, name='logout'),
        path('posts/logout/', views.logout_view, name='logout'),
    ];