from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer
from .permissions import IsPostOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')
    serializer_class = PostSerializer
    permission_classes = [IsPostOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        print(request.data)
        username = request.data['author']['username']
        user = User.objects.get(username=username)
        title = request.data['title']
        content = request.data['content']
        date_posted = request.data['date_posted']
        try:
            post = Post.objects.create(title=title, content=content, date_posted=date_posted)
            post.author = user
            post.save()
            serialized_post = PostSerializer(post, context={'request': request})
            return Response(serialized_post.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': e.__str__()}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def get_posts_by_user(request, username):
#     user = get_object_or_404(User, username=username)
#     return Response({
#         'user': {
#             'username': user.username,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#         },
#         'posts': 'posts will be here'
#     })


class GetPostsByUser(generics.GenericAPIView):
    queryset = Post.objects.all()

    def get(self, request, username, *args, **kwargs):
        posts = Post.objects.filter(author__username=username)
        serialized_posts = PostSerializer(posts, many=True, context={'request': request})
        return Response(serialized_posts.data,)
