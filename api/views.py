from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly

class UserList(generics.ListAPIView):
      queryset = User.objects.all()
      serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset = Post.objects.all()
      serializer_class = PostSerializer
      permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


