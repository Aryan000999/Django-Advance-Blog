from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from ...models import Post,Category
from rest_framework.reverse import reverse
from .serializer import PostSerializer,CategorySerializer
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .pagination import DefaultPagination
from .filters import PostFilter
# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view,permission_classes
"""
FBV for api
"""
# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_list(request):
#     """
#     getting post list with get request
#     aded new post with post requests
#     """
#     if request.method=="GET":
#         posts=Post.objects.filter(status=True)
#         serializer=PostSerializer(posts,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     elif request.method=="POST":
#         serializer=PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(author=request.user)
#         return Response(serializer.data,status=status.HTTP_201_CREATED)



# @api_view(['GET','PUT','DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_detail(request,id):
#     """
#     getting a post item with get.
#     authenticate user can send put and delete request for edit and delete that post.
#     """
#     post=get_object_or_404(Post,status=True,pk=id)
#     if request.method=="GET":
#         serializer=PostSerializer(post)
#         return Response(serializer.data)
#     elif request.method=="PUT":
#         serializer=PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status.HTTP_200_OK)
#     elif request.method=="DELETE":
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
"""
the class for detail of posts and base genericviews
"""
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class=PostSerializer
#     queryset=Post.objects.filter(status=True)

# class PostList(ListCreateAPIView):
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     serializer_class=PostSerializer
#     queryset=Post.objects.filter(status=True)
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
    
"""
the main viewsets for post class
"""
class PostViewSet(ModelViewSet):
    serializer_class=PostSerializer
    queryset=Post.objects.filter(status=True)
    permission_classes=[IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    filter_backends=[DjangoFilterBackend,SearchFilter]
    filterset_class=PostFilter
    search_fields=["title","content"]
    ordering=["-published_date"]
    pagination_class=DefaultPagination
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.profile)
    def retrieve(self, request, *args, **kwargs):
        response=super().retrieve(request, *args, **kwargs)
        response.data["post_list"]=reverse("blog:api-v1:post-list", request=request)
        return response

class CategoryViewSet(ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    permission_classes=[IsAuthenticatedOrReadOnly]
    





