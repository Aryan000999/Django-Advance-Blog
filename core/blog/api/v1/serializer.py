from rest_framework import serializers
from ...models import Post,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","name"]

class PostSerializer(serializers.ModelSerializer):
    snippet=serializers.ReadOnlyField(source="get_snippet")
    reative_url=serializers.URLField(source="get_absolute_api_url",read_only=True)
    absolute_url=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields=["id","title","author","content","status","category","created_date","updated_date","snippet","reative_url","absolute_url"]
        read_only_fields = ['author']
    def get_absolute_url(self,obj):
        request=self.context.get("request")
        return request.build_absolute_uri(obj.pk)
    def to_representation(self, instance):
        request=self.context.get("request")
        rep= super().to_representation(instance)
        rep["category"]=CategorySerializer(instance.category).data["name"]
        if request.parser_context.get('kwargs').get("pk"):
            rep["state"]="single"
            rep.pop("snippet")
            rep.pop("reative_url")
            rep.pop("absolute_url")
        else:
            rep["state"]="list"
            rep.pop("content")

        return rep

        