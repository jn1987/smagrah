from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import posts
from .forms import Post_Form
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

def new(request):
  if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.title = request.user
            # post.published_date = timezone.now()
            post.save()
            # return redirect('index', pk=post.pk)
  else:
        form = Post_Form()
  return render(request, 'posts/new.html', {'form': form})