from django.urls import path, include
from rest_framework import routers

from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView
)
from . import views
from .api_views import PostViewSet, GetPostsByUser


router = routers.DefaultRouter()
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # .as_view because we need to convet class to a view (Part 10)
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),  # Part 11 (FIltering Posts By User)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Part 10 detail view.. pk=primary key, we used it because thats what the detail view expects it to be in order to grab that specific object
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # post_form.html (<model>_form.html)
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),  # Part 10 update view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),  # Part 10 delete view
    path('about/', views.about, name='blog-about'),
    path('api/users-model/', include('users.urls')),
    path('api/post-model/', include(router.urls), name='post-model'),
    path('api/post-model/<username>/posts/', GetPostsByUser.as_view(), name='get-posts-by-user'),
]
