from django.contrib import admin
from accounts.models import User,Profile
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model=User
    list_display=['email','is_superuser',"is_active"]
    list_filter=['is_superuser',"is_active"]
    search_fields=['email']
    ordering=['-created_date']
    fieldsets=(
        ('authentication',{"fields":("email","password")}),
        ('permissions',{"fields":("is_staff","is_superuser","is_active")}),
        ('group permissions',{"fields":("groups","user_permissions")}),
        ('important date',{"fields":("last_login",)}),
        
    )
    add_fieldsets=(
        ('authentication',{"fields":("email","password1","password2","is_staff","is_superuser","is_active")}),

    )
admin.site.register(Profile)