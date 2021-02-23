from django.urls import path

from . import views

urlpatterns=[
    path('', views.show_csgo_stats, name="csgo_stats_show"),
]