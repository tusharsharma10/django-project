from django.urls import path
from . views2 import articleList,articleDetail
from . views2 import ArticleAPIView
from . views2 import ArticleDetailsAPIView

from . views import GenericAPIView

urlpatterns = [
    #path('detail/<int:pk>/',articleDetail),
    path('detail/<int:pk>/',ArticleDetailsAPIView.as_view()),
    #path('',ArticleAPIView.as_view()),
    path('generic/',GenericAPIView.as_view()),
   # path('',articleList),

]