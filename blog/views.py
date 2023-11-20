from django.shortcuts import render
from . import data
import operator


# Create your views here.

def index(req):
    return render(req, "blog/index.html", {
        "posts": data.post_data
    })

def latest(req):
    lastest_post = sorted(data.post_data, key=operator.itemgetter('date'), reverse=True)
    return render(req, "blog/index.html", {
        'posts': lastest_post
    })
def top(req):
    top_post = sorted(data.post_data, key=operator.itemgetter('views'), reverse=True)
    return render(req, "blog/index.html", {
        'posts': top_post
    })


def post(req, slug):
    
    current_post = [x for x in data.post_data if x['slug'] == slug] 
    
    return  render(req, "blog/post.html", {
        "post": current_post[0] 
    })