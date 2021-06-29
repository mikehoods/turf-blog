from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . models import Post
from django.urls import reverse_lazy

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return redirect('post-detail', post.pk)

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-pub_date']

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ('title', 'body')
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

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
