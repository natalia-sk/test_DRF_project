from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

@api_view(["GET"])
def list_articles(request):
    articles = Article.objects.all()
    serializers = ArticleSerializer(articles, many=True)
    content = {
        "articles": serializers.data,
    }
    return Response(content)
