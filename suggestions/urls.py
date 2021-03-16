from django.urls import path

from . import views

urlpatterns=[
    path('', views.show_suggestions, name="show_suggestions"),
    path('create/', views.create_suggestion, name="create_suggestion")
]
