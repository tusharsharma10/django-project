from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from . models import Article
from .modelSerializer import ArticleModelSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def articleList(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)



@csrf_exempt
def articleDetail(request,pk):
    if request.method == 'GET':
        articles = Article.objects.get(pk=pk)
        serializer = ArticleModelSerializer(articles)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)


