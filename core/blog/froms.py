from django import forms
from .models import Post
#post create form

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=["image","created_date","updated_date","author"]
