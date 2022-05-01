from api_basics.models import Article
from api_basics.serializer import ArticleSerializer
from rest_framework .renderers import JSONRenderer
from rest_framework.parsers import JSONParser

a = Article(1,'Sample','Wayne Rooney','wayne@gmail.com')
a.save()

serializer = ArticleSerializer(a)
content = JSONRenderer().render(serializer.data)

print(content)