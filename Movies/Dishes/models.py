from django.db import models

# Create your models here.

dishes=[
{"id":1,"name":"Kanji","price":55,"Category":"Veg"},
{"id":2,"name":"biriyani","price":150,"Category":"Non Veg"},
{"id":3,"name":"omelet","price":25,"Category":"Non Veg"},
{"id":4,"name":"Meal","price":50,"Category":"Non Veg"},
{"id":5,"name":"Portta","price":15,"Category":"Veg"},

]

class Dishes(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.CharField(max_length=100)