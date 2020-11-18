from django.shortcuts import render
from django.http import HttpResponse

def show_articles(request):
    return render(request, "book_reviews/show_articles.html")