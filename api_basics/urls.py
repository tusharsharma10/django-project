from django.urls import path
from . views import articleList


urlpatterns = [
    path('',articleList),
]