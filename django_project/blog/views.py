"""
This file is used to
This is to setup the routing logic for our site lives

"""

from django.shortcuts import render #this is used for our templates
# from django.http import HttpResponse #http response can be used for testing a view.
from .models import Post # the . just mean it is in the current package
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )

# say ou are making a blog. lets make some dummy data to see what it would look like

"""
Test posts
posts = [
    {
        'author': 'alexD',
        'title': 'helloWorld',
        'content':'hello world',
        'date_posted':'August, 10, 2019'
    },
    {
        'author': 'Jamey',
        'title': 'helloAll',
        'content':'hello All',
        'date_posted':'August, 11, 2019'
    }

]
"""


# Create your views here.


def home(request):
    # returns what we want the user to see when  they hit this route
    context = {
        'posts':Post.objects.all() # now this is accessible within the template because we passed it into the render's
        # context
        # argument
    }
    return render(request,'blog/home.html',context) # context option lets us pass in content

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html to alter the ref. html page
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """allows us to set the author before running the form validation."""
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """allows us to set the author before running the form validation."""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    # returns what we want the user to see when  they hit this route
    return render(request,'blog/about.html', {'title':'about'})

"""different kinds of class based views. Django has many built. List view, detail view, etc"""
