from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from blog.models import Post

class PostCreateView(CreateView):
    model = Post
    fields = "_ _all _ _"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"
     
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class PostUpdateView(UpdateView):
    model = Post
    fields =  "_ _all _ _"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_form.html"

class PostDeleteView(DeleteView):
    model = Post
    fields = "_ _all _ _"
    success_url = reverse_lazy("blog:all")
    template_name = "blog/post_confirm_delete.html"
