from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from post.serializers import PostSerializer
from post.models import Post, Like

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class RetrievePostView(RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class AllPostsView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CreatePostView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        post = get_object_or_404(Post, id=pk)
        like = Like.objects.filter(post=post, from_user=request.user).first()
        if not like:
            Like.objects.create(post=post, from_user=request.user)
        else:
            like.deleted = not like.deleted
            like.save()

        data = PostSerializer(post).data
        return Response(data)
