from django.db import models

class Suggestions(models.Model):

    title = models.CharField(max_length=32)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    