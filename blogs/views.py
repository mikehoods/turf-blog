from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . models import Post
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ('title', 'author', 'body')
    success_url = reverse_lazy('home')
