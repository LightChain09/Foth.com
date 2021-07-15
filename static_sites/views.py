from django.shortcuts import render


def show_legal_page(request):
    return render(request, 'static_sites/legal.html')


def show_about_page(request):
    return render(request, 'static_sites/about.html')


def show_landing_page(request):
    return render(request, 'static_sites/index.html')


def show_projects_page(request):
    return render(request, 'static_sites/projects.html')