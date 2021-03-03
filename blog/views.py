from django.shortcuts import render
from .models import BlogArticle

def show_blog_posts(request):

    articles = BlogArticle.objects.order_by("publish_date")

    return render(request, "blog/show_blog_posts.html", {"articles": articles})


def post_detail(request, title):

    article = BlogArticle.objects.get(title=title)

    return render(request, "blog/post_detail.html", {"article": article})