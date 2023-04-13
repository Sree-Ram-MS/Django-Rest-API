from rest_framework import serializers
from .models import Dishes
from django.contrib.auth.models import User


class Dishserializer(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField()



class DishModelSer(serializers.ModelSerializer):
    class Meta:
        model=Dishes
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)