from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
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

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class EditPostView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ('title', 'body')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
