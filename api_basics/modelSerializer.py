from rest_framework import serializers
from . models import Article

class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','title','author']