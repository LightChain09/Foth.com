from django.db import models

class ThoughtArticles(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField(auto_now=True)
    article_content = models.CharField(max_length=25000)