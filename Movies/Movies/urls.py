"""Movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from api.views import Movielist,Movie,Films,FilmItem,UserCreation
from Dishes.views import Dishlist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',Movielist.as_view()),
    path('dishes/',Dishlist.as_view()),
    # path('dishes/<int:did>',Dish.as_view()),
    path('movies/<int:mid>',Movie.as_view()),
    path('Film',Films.as_view()),
    path('Film/<int:fid>',FilmItem.as_view()),

    path('Reg',UserCreation.as_view()),
]
