from django.shortcuts import render

def show_legal_page(request):
    return render(request, 'legal.html')