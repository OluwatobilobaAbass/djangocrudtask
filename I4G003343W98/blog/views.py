<<<<<<< HEAD
=======
from django.shortcuts import render
from django.urls import reverse_lazy
>>>>>>> a7319c70caa8f78d046d12419014e5225e76aa05
from django.views import generic
from .models import Post
from django.urls import reverse_lazy

<<<<<<< HEAD

# Create your views here.
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostListView(generic.ListView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy('blog:all')
    template_name = 'post_list.html'

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy('blog:all')
    template_name = 'post_form.html'

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy('blog:all')
    template_name = 'post_form.html'
class PostDeleteView(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy('blog:all')
    template_name = 'post_confirm_delete.html'
=======
class PostListView(generic.ListView):
    model = Post
    template_name = "templates/blog/post_list.html"

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "templates/blog/post_form.html"

class PostDetailView(generic.DetailView):
    model = Post
    template_name = "templates/blog/post_detail.html"
class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "templates/blog/post_form.html"

class PostDeleteView(generic.DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "templates/blog/post_delete.html"
>>>>>>> a7319c70caa8f78d046d12419014e5225e76aa05
