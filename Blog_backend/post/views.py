from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from account.models import Profile


@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def postOverview(request):
    api_urls = {
        "Post overview": "api/",
        "View all post": "api/posts/get",
        "add post": "api/posts/add",
        "view single post": "api/posts/get/:pk",
        "update post": "api/posts/get/:pk/update",
        "delete post": "api/posts/get/:pk/delete",
        "like post": "api/posts/get/:pk/like",
        "all comment": "api/posts/get/:post_id/comment/get",
        "add comment": "api/posts/get/:post_id/comment/add",
        "comment update": "api/posts/get/:post_id/comment/get/:pk/update",
        "comment delete": "api/posts/get/:post_id/comment/get/:pk/delete",
        "comment like": "api/posts/get/:post_id/comment/get/:pk/like",
    }
    return Response(api_urls, status=status.HTTP_200_OK)


# POST
@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def viewAllPost(request):
    posts = Post.objects.order_by('?').all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def addPost(request):
    post = PostSerializer(data=request.data)
    post.is_valid(raise_exception=True)
    post.save()

    return Response(post.data, status=status.HTTP_200_OK)
    

@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def viewPost(request, pk):
    post = Post.objects.get(pk=pk)

    if post is not None:
        post.views += 1
        post.save()
        serializer = PostSerializer(post)

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def updatePost(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    if post is not None:
        if post.user_id == user.id:
            serializer = PostSerializer(instance=post, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@permission_classes([permissions.IsAuthenticated])
@api_view(['DELETE'])
def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    if post is not None:
        if post.user_id == user.id:
            post.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def likePost(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    if post is not None and user is not None:
        if user.id not in post.likes.all():
            post.likes.add(user.id)
        else:
            post.likes.remove(user.id)
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# COMMENT
@permission_classes([permissions.AllowAny])
@api_view(['GET'])
def viewAllComment(request, post_id):
    comments = Comment.objects.filter(post_id=post_id).all()
    serializer = CommentSerializer(comments, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def addComment(request, post_id):
    user = request.user
    data = {
        "post_id": post_id,
        "content": str(request.data.get("content")),
        "user_id": user.id
    }
    comment = CommentSerializer(data=data)
    comment.is_valid(raise_exception=True)
    comment.save()

    return Response(comment.data, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
@api_view(['PUT'])
def updateComment(request, post_id, pk):
    comment = Comment.objects.get(pk=pk)
    post = Post.objects.get(pk=post_id)
    user = request.user

    if comment is not None and comment.post_id == post:
        if comment.user_id == user.id:
            serializer = CommentSerializer(instance=comment, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@permission_classes([permissions.IsAuthenticated])
@api_view(['DELETE'])
def deleteComment(request, post_id, pk):
    comment = Comment.objects.get(pk=pk)
    post = Post.objects.get(pk=post_id)
    user = request.user

    if comment is not None and comment.post_id == post:
        if comment.user_id == user.id:
            comment.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@permission_classes([permissions.IsAuthenticated])
@api_view(['POST'])
def likeComment(request, post_id, pk):
    comment = Comment.objects.get(pk=pk)
    post = Post.objects.get(pk=post_id)
    user = request.user

    if comment is not None and comment.post_id == post:
        if user.id not in comment.likes.all():
            comment.likes.add(user.id)
        else:
            comment.likes.remove(user.id)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)