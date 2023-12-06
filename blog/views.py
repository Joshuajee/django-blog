from django.shortcuts import render, HttpResponseRedirect
from blog.models import Posts, Author
from django.db.models import F
from .forms import SignupForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(req):
    print(req.user.is_authenticated)
    posts = Posts.objects.all().values()
    return render(req, "blog/index.html", {
        "posts": posts,
    })

def latest(req):
    lastest_post = Posts.objects.all().order_by("-date")
    return render(req, "blog/index.html", {
        'posts': lastest_post
    })
def top(req):
    top_post = Posts.objects.all().order_by("-views")
    return render(req, "blog/index.html", {
        'posts': top_post
    })


def post(req, slug):
    
    current_post = Posts.objects.get(slug= slug)
    
    Posts.objects.filter(slug= slug).update(views=F('views') + 1)
    
    return  render(req, "blog/post.html", {
        "post": current_post
    })
    
def signup(req):
    form = SignupForm()
    error = False
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            try:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=email, email=email, password=password)
            except:
                error = True
                pass
        else:
            pass
            

    return  render(req, "blog/signup.html", {
        "form": form,
        "hasError": error
    })
    
    
    
def login_view(req):
    
    form = LoginForm() 
    
    if req.method == "POST":
        loginForm  = LoginForm(req.POST)
        if loginForm.is_valid():
            email = loginForm.cleaned_data['email']
            password = loginForm.cleaned_data['password']
            
            try:        
                user = authenticate(username=email, password=password)
                print(user)
                if user == None:
                    return render(req, "blog/login.html", {
                        "form": form,
                        "error": "Wrong Email or Password"
                    })
                else:
                    login(req, user)
                    try:
                        return HttpResponseRedirect(req.GET['next'])
                    except:
                        return HttpResponseRedirect("/")
            except:
                return render(req, "blog/login.html", {
                    "form": form,
                    "error": "Wrong Email or Password"
               })
                
    return render(req, "blog/login.html", {
        "form": form,
    })
    
def logout_view(req): 
    logout(req)
    return HttpResponseRedirect("/")
            

@login_required(login_url="/login")
def create_post(req):
    
    if req.method == 'POST':
        author = req.POST['author']
        title = req.POST['title']
        content = req.POST['content']
        new_post = Posts(author=author, title=title, content=content)
        
        new_post.save()


    return  render(req, "blog/create-post.html")