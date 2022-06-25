from dataclasses import field
from re import template
from django.views.generic.edit import CreateView
from .models import Post

model = Post

fields = ['title',
'description'
]
template_name = 'home.html'
