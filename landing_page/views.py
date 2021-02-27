from django.shortcuts import render
import datetime

def calculate_age(birth):
    now = datetime.datetime.now()
    difference = now - birth

    days = difference.days

    years = days / 365
    
    return years


def show_landing_page(request):

    age = calculate_age(datetime.datetime(year=2002, month=9, day=3, hour=14))

    return render(request, 'landing_page/index.html', {"age": age})

