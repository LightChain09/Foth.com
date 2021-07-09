from django.shortcuts import render
import datetime

def calculate_age(birth):
    now = datetime.datetime.now()
    difference = now - birth

    days = difference.days

    return days / 365


def show_legal_page(request):
    return render(request, 'static_sites/legal.html')


def show_about_page(request):
    age = calculate_age(datetime.datetime(year=2002, month=9, day=3, hour=14))
    return render(request, 'static_sites/about.html', {"age": age})


def show_landing_page(request):
    return render(request, 'static_sites/index.html')