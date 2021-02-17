from django.db import models


class BookReviewArticle(models.Model):
    book_title = models.CharField(max_length=64)
    introduction = models.CharField(max_length=2000, default="*Introduction*")
    review_content = models.CharField(max_length=25000)
    article_date = models.DateField(auto_now=True)
