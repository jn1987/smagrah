from django.shortcuts import render
from django.http import HttpResponse
from .models import posts
# Create your views here.
def index(request):
     Posts = posts.objects.all()

     context = {
        'title':'All Posts',
        'posts':Posts
     }

     return render(request,'posts/index.html',context)   

def details(request,id,title):
  
     Post = posts.objects.get(slug=title)

     context = {
       'post':Post
        }

     return render(request,'posts/details.html',context)