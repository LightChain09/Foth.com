from django.shortcuts import render

from .models import BookReviewArticle

def show_articles(request):
    book_reviews = BookReviewArticle.objects.all()
    return render(request, "book_reviews/show_articles.html", {"book_reviews": book_reviews})
