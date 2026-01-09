from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'image', 'title', 'content', 'user_id', 'timestamp', 'last_updated', 'views', 'likes', 'post_like']
        extra_kwargs = {'id': {'read_only': True}, 'post_like': {'read_only': True}}


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'content', 'user_id', 'likes', 'comment_like']
        extra_kwargs = {'id': {'read_only': True}, 'comment_like': {'read_only': True}}