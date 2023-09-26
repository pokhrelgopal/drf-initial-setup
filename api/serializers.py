from rest_framework import serializers
from .models import Comment, BlogPost, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            "id": {"read_only": True},
            "email": {"required": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {"required": True, "write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    comment_set = serializers.SerializerMethodField()
    author = UserSerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            "id",
            "title",
            "content",
            "author",
            "publication_date",
            "last_updated",
            "categories",
            "image",
            "comment_set",
        ]

    def get_comment_set(self, obj):
        comments = Comment.objects.filter(post=obj)
        return CommentSerializer(comments, many=True).data


# NOTE: It needs post_id and text, user is automatically selected.
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    blog_id = serializers.IntegerField(source="post.id", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "blog_id", "author", "text", "timestamp"]
