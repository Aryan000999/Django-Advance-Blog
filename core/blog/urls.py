from django.urls import path
from . import views
app_name="blog"
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("posts/",views.PostListView.as_view(),name="posts"),
    path("post/create/",views.CreatePostView.as_view(),name="create_post")
]