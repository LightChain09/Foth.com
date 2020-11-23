from django.urls import path

from . import views

urlpatterns=[
    path('', views.show_thought_posts, name="show_thought_posts")
]