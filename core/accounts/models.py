from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    pass


class User(AbstractBaseUser,PermissionsMixin):
    """
    the User model for project with email(password in the AbstractBaseUser)
    """
    email=models.EmailField(max_length=255,unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    objects=UserManager()
    def __str__(self):
        return self.email


