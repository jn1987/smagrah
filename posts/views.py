from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import posts
from .forms import Post_Form
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.postgres.search import SearchVector
# Create your views here.
def index(request):
     Posts = posts.objects.all()

     context = {
        'title':'All Posts',
        'posts':Posts
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
            # post.title = request.user
            # post.published_date = timezone.now()
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
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)
            # items = posts.objects.annotate(search=SearchVector('user')).filter(search= user)
            return redirect('index')
            
  else:
        form = AuthenticationForm()
  return render(request, 'posts/login.html', {'form': form})