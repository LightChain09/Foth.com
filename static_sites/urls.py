from django.urls import path

from . import views

urlpatterns=[
    path('/legal/', views.show_legal_page, name="show_legal_page")
]