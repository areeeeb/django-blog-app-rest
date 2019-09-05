from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post  # .models because it is in the same directory
from django.contrib.auth.models import User


# This is home view with function based view (older one)
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# recreating home view with class based view below
class PostListView(ListView):
    model = Post

    # by default, it looks for a template at <app>/<model>_<viewtype>.html (blog/post_list.html), but we can change it
    template_name = 'blog/home.html'

    # By default all our posts are called ObjectList by ListView, so we need to change it too
    context_object_name = 'posts'

    ordering = ['-date_posted']  # '-' sign to make it go from newest to oldest

    paginate_by = 5  # Display 2 posts per page (Part 11)


class UserPostListView(ListView):  # Part 11 (Filtering Posts By User)
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))  # get the User with the usrename that is passed in the URL
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    '''in post_detail.html, we call every post an object because it is the convention so we dont have to reset the names
     like before'''


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author for current instance of form to the user logged in
        return super().form_valid(form)


# UserPassesTestMixin so that other users cant edit your posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # for UserPassesTestMixin
        post = self.get_object()  # it is the UpdateView method to get the current post which is getting updated

        if self.request.user == post.author:  # self.request.user is the current logged in user
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # on success, send the user to the homepage

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
