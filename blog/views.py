from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

# list view for reading specific blogs
class PostDetailView(DetailView):
    model = Post

# list view  for writing blogs
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] # add a field for pictures

 # list view  for updating blogs
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content'] # add a field for pictures

    # autmoatically makes home is signed in as the submitter
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

# function view to create about page
def about(request):
    return render(request, 'blog/about.html', {'title':"About"})

# class view to display update and delete posts


