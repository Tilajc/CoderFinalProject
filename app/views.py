from django.shortcuts import render
from django.views.generic import CreateView, ListView

from app.models import Post


# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'app/about_me.html')

class CreatePost(CreateView):
    model = Post
    success_url = "/app/posts"
    template_name = "app/create_post.html"
    fields = ['title', 'version', 'subtitle', 'body', 'author']

class posts(ListView):
    model = Post
    template_name = "app/posts.html"

def update_post(request):
    return render(request, 'app/update_post.html')

def delete_post(request):
    return render(request, 'app/delete_post.html')

def comments(request):
    return render(request, 'app/comment.html')