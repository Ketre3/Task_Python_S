from post.models import Post

from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", 'title', 'text', 'likes')

    def get_likes(self, post: Post):
        return len(post.likes.filter(deleted=False))
