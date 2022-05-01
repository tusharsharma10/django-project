from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from . models import Article
from .modelSerializer import ArticleModelSerializer
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Class Based Views
class ArticleAPIView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ArticleModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailsAPIView(APIView):
    def get(self,request,pk):
        articles = Article.objects.get(pk=pk)
        serializer = ArticleModelSerializer(articles)
        return Response(serializer.data)

    def post(self,request,pk):
        serializer = ArticleModelSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Function based views
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


