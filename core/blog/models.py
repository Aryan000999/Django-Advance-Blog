from django.db import models
from django.utils import timezone
from accounts.models import Profile
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    '''
    this is a class to define posts for blog app
    '''
    author=models.ForeignKey(Profile,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    status=models.BooleanField(default=False)
    category=models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)
    pubished_date = models.DateTimeField(default=timezone.now)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_snippet(self):
        return self.content[:300]
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail",kwargs={'pk':self.pk})

class Category(models.Model):
    '''
    this is a class to define category for blog app
    '''
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

