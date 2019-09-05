from rest_framework import serializers

from .models import Post
from users.serializers import UserSerializer


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'title', 'content', 'date_posted', 'author']
