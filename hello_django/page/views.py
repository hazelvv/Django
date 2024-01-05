from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk' ##최신글의 내용을 상단에 배치
    template_name = 'page/index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'page/single_post_page.html'