from dataclasses import field
from re import template
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Post

model = Post

fields = ['title',
'description'
]
template_name = 'base.html'

class PostListView(ListView):
    model: Post
    template_name = 'list.html'
