from django.urls import path

from . import views

urlpatterns=[
    path('', views.show_blog_posts, name="show_blog_posts"),
    path('<int:id>', views.post_detail, name="post_detail"),
]
