from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import posts
from django.contrib.auth.models import User
from .forms import Post_Form
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.postgres.search import SearchVector
# Create your views here.
def index(request):
     Posts = posts.objects.all()
     username = request.user.username
     context = {
        'title':'All Posts',
        'posts':Posts,
        'username':username
     }

     return render(request,'posts/index.html',context)   

def details(request,id,slug):
  
     Post = posts.objects.get(id=id)

     context = {
       'post':Post
        }

     return render(request,'posts/details.html',context)

def new(request):
  if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author=request.user
            post.save()
        return redirect('index')

  else:
        form = Post_Form()
  return render(request, 'posts/new.html', {'form': form})


def search(request):
      if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        

        items = posts.objects.annotate(search=SearchVector('title','slug','body','tags')).filter(search= q)  
      #   items = posts.objects.filter(slug_search = q)
        return render(request, 'posts/search.html',
                      {'items': items, 'query': q})
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
      else:
        message = 'You submitted an empty form.'
      return HttpResponse(message)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'posts/signup.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)
            user_id= User.objects.get(username=username).pk
            # items = posts.objects.annotate(search=SearchVector('author_id')).filter(search=user_id)
            # items = posts.objects.get(author_id=user_id)
            items = posts.objects.filter(author_id=user_id)
            if (items):
             return render(request,'posts/user_login.html', 
                                  {'items':items, 'username':username})
            else:
              return render(request,'posts/user_login.html', 
                                  {'items':[], 'username':username})
                  
  else:
        form = AuthenticationForm()
  return render(request, 'posts/login.html', {'form': form})

def logout_view(request):
    username = request.user.username
    logout(request)
    return render(request,'posts/user_logout.html',{'username':username})

def my_posts(request):
    user_id= request.user.pk
    username = request.user.username
    items = posts.objects.filter(author_id=user_id)
    if (items):
      return render(request,'posts/myposts.html', 
              {'items':items, 'username':username})
    else:
      return render(request,'posts/myposts.html', 
              {'items':[], 'username':username})