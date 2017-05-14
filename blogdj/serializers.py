from django.conf.urls import url
from django.contrib.auth.models import User

from rest_framework import serializers,routers, viewsets

from blogdj.models import Article


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Article
        fields =('titel','body','image', 'author')







