from rest_framework import serializers
from ...models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=["title","content","author","status","category","created_date","updated_date"]