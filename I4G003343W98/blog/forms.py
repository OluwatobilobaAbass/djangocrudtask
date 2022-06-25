from dataclasses import field
from django import forms
from .models import BlogApp

class BlogAppForm(forms):
class Meta:
    model = BlogApp

    fields = [
        "title",
        "description",
    ]