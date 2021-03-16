from django.shortcuts import render
from .models import ThoughtArticles

def show_thought_posts(request):
    articles = ThoughtArticles.objects.all()
    return render(request, "thoughts/show_thought_posts.html", {"articles": articles})