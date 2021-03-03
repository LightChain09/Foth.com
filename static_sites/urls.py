from django.urls import path

from . import views

urlpatterns=[
    path('', views.show_landing_page, name="show_landing_page"),
    path('legal/', views.show_legal_page, name="show_legal_page")
]