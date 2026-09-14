from django.db import models
from accounts.models import User
# Create your models here.
class Post(models.Model):
    '''
    this is a class to define posts for blog app
    '''
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(null=True,blank=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    status=models.BooleanField()
    categoty=models.ForeignKey("Category",on_delete=models.SET_NULL,null=True)

    pubished_date=models.DateTimeField()
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    '''
    this is a class to define category for blog app
    '''
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

