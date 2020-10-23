from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    paginate_by = 2


# list view for reading specific blogs
class PostDetailView(DetailView):
    model = Post


# list view  for writing blogs
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content'] # add a field for pictures
        # autmoatically makes the signed in user as the author
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


 # list view  for updating blogs and only if ithe user created the blog
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content'] # add a field for pictures


    # check current user is author
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


    # autmoatically makes home is signed in as the submitter
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)


# list view deleting view
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # add a route so when the post is successfully deleted
    success_url = '/'


    # check current user is author
    def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            else:
                return False


# function view to create about page
def about(request):
    return render(request, 'blog/about.html', {'title':"About"})

# class view to display update and delete posts


