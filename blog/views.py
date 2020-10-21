from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# function view to create home page
def home(request):
    context = {
        'posts':Post.objects.all
    }
    return render(request, 'blog/home.html', context)


# list view for home page
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #setting attribtue equal to posts in home function
    ordering = ['-date_posted']

# list view
class PostDetailView(DetailView):
    model = Post


# function view to create about page
def about(request):
    return render(request, 'blog/about.html', {'title':"About"})

# class view to display update and delete posts


