from django.shortcuts import render
from django.http import HttpResponse

def show_articles(request):
    return HttpResponse("HalloTest123")