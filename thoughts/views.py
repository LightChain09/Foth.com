from django.shortcuts import render

def show_thought_posts(request):
    return render(request, "thoughts/show_thought_posts.html")