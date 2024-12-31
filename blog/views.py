# from django.shortcuts import render
# from django.views import generic
# from .models import Post

# # Define the view
# class PostList(generic.ListView):
#     queryset = Post.objects.all()
#     template_name = "post_list.html"

from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    template_name = "blog/post_list.html"
    
    def get_queryset(self):
        queryset = Post.objects.order_by('-created_on')
        print("Number of posts:", queryset.count())  # Debug print
        print("Available posts:", list(queryset.values('title', 'author')))  # More detailed debug info
        return queryset