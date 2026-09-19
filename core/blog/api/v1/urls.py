from django.urls import path
from . import views
urlpatterns=[
    path("post/",views.post_list,name="post_list"),
    path("post/<int:id>",views.post_detail,name="post_detail"),
    path("post/new",views.new_post,name="new_post")
]