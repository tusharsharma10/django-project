from django.urls import path
from . views import articleList,articleDetail


urlpatterns = [
    path('detail/<int:pk>/',articleDetail),
    path('',articleList),

]