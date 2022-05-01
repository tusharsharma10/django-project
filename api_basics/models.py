from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    author = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title