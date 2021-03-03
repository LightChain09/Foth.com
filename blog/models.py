from django.db import models

class BlogArticle(models.Model):
    title = models.CharField(max_length=64)
    publish_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
