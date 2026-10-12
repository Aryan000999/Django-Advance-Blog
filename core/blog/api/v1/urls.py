from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views
# urlpatterns=[
#     path("post/",views.PostList.as_view(),name="post_list"),
#     path("post/<int:pk>",views.PostDetail.as_view(),name="post_detail"),
    
# ]
app_name="api-v1"
router=DefaultRouter()
router.register("post",views.PostViewSet,basename="post")
router.register("category",views.CategoryViewSet,basename="category")
urlpatterns=router.urls