"""webservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as userViews
from django.contrib.auth import views as authViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("static_sites.urls"), name="static-sites"),
    path('csgo/', include("csgo.urls"), name="csgo"),
    path('poker/', include("poker.urls"), name="poker"),
    path('blog/', include("blog.urls"), name="blog"),
    path('suggestions/', include("suggestions.urls"), name="suggestions"),
    path('register/', userViews.registerUser, name="register"),
    path('login/', authViews.LoginView.as_view(template_name="users/loginUser.html",), name="login"),
    path('logout/', authViews.LogoutView.as_view(template_name="users/logoutUser.html"), name="logout"),
    path('profile/', userViews.userProfile, name="userProfile"),
]
