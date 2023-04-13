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
from api.views import Movielist,Movie,Films,FilmItem,UserCreation,MovieAPI,MoviesApiMV
from Dishes.views import Dishlist,Dish,Dishes,DishItem

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken import views


router=DefaultRouter()
router.register('Movieapi',MovieAPI,basename='mapi')
router.register('MVapi',MoviesApiMV,basename='mvapi')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('movies/',Movielist.as_view()),
    path('movies/<int:mid>',Movie.as_view()),
    path('Film',Films.as_view()),
    path('Film/<int:fid>',FilmItem.as_view()),

    path('Reg',UserCreation.as_view()),

    path('Dish/',Dishes.as_view()),
    path('Dish/<int:fid>',DishItem.as_view()),
    path('dishes/',Dishlist.as_view()),
    path('dishes/<int:mid>',Dish.as_view()),


    path('token-auth/', views.obtain_auth_token)
]+router.urls
