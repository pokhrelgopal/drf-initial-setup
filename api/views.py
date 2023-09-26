from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Comment, BlogPost, Category
from .serializers import (
    BlogSerializer,
    CategorySerializer,
    CommentSerializer,
    UserSerializer,
)
from api.permissions import CustomPermission, IsAdminOrReadOnly


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    permission_classes = [CustomPermission]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.request.data.get("post_id")

        try:
            post = BlogPost.objects.get(pk=post_id)
        except BlogPost.DoesNotExist:
            raise serializers.ValidationError({"postId": "Invalid postId"})

        serializer.save(author=self.request.user, post=post)


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
