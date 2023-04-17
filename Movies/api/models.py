from django.db import models
from django.contrib.auth.models import User

# Create your models here.
movies=[
    {"id":1,"name":"Dada","year":2023,"Director":"Ganesh","Genre":"Feel Good"},
    {"id":2,"name":"Vaaranam Aayiram","year":2008,"Director":"GVM","Genre":"Romantic"},
    {"id":3,"name":"Dia","year":2020,"Director":"Ashok","Genre":"Sadist"},
    {"id":4,"name":"mucize","year":2015,"Director":"Mahsun","Genre":"Drama"},
    {"id":5,"name":"Kirik Party","year":2016,"Director":"Rishab Shetty","Genre":"Comedy"},
]

class Movies(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    Director=models.CharField(max_length=100)
    Genre=models.CharField(max_length=100)
    img=models.ImageField(upload_to="Film Poster",null=True)

class Review(models.Model):
    review=models.CharField(max_length=500)
    rating=models.FloatField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)