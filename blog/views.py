from django.shortcuts import render
from .models import BlogArticle

def show_blog_posts(request):

    articles = BlogArticle.objects.order_by("publish_date")

    return render(request, "blog/show_blog_posts.html", {"articles": articles})


def post_detail(request, id):

    article = BlogArticle.objects.get(id=id)

    return render(request, "blog/post_detail.html", {"article": article})