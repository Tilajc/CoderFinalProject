from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from app.models import Post, Comment
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

def is_admin(user):
    return user.is_authenticated and user.is_superuser

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'app/about_me.html')

@method_decorator(user_passes_test(is_admin), name='dispatch')
class CreatePost(CreateView):
    model = Post
    success_url = "/app/posts"
    template_name = "app/create_post.html"
    fields = ['title', 'version', 'subtitle', 'body', 'img']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class Posts(ListView):
    model = Post
    template_name = "app/posts.html"

class PostDetail(DetailView):
    model = Post
    template_name = "app/post_detail.html"

@method_decorator(user_passes_test(is_admin), name='dispatch')
class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = "/app/posts"
    template_name = "app/create_post.html"
    fields = ["title", 'version', 'subtitle', 'body', 'img']

@method_decorator(user_passes_test(is_admin), name='dispatch')
class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/app/posts"
    template_name = "app/delete_post.html"

class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    success_url = "/app/posts"
    template_name = "app/create_comment.html"
    fields = ["post", "message"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)