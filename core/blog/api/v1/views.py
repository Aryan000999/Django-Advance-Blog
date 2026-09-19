from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework import status
from ...models import Post
from .serializer import PostSerializer
@api_view()
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(requset):
    posts=Post.objects.filter(status=True)
    serializer=PostSerializer(posts,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request,id):
    post=get_object_or_404(Post,status=True,pk=id)
    if request.method=="GET":
        serializer=PostSerializer(post)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)
    elif request.method=="DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])  
def new_post(request):
    if request.method=="POST":
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

