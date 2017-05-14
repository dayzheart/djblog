
from rest_framework import viewsets

from blogdj.models import Article
from blogdj.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer