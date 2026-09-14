from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView,CreateView
from .models import Post
from .froms import PostCreateForm
# Create your views here.

class IndexView(TemplateView):
    template_name="blog/blog_index.html"

class PostListView(ListView):
    model=Post
    context_object_name="posts"
    def get_queryset(self):
        posts=super().get_queryset().filter(status=True).order_by("-pubished_date")
        return posts
    

class CreatePostView(CreateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy("blog:posts")
    def form_valid(self, form):
        form.instance.author=self.request.user
        form.save()
        return super().form_valid(form)