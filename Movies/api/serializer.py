from rest_framework import serializers
from .models import Movies
from django.contrib.auth.models import User


class Movieserializer(serializers.Serializer):
    name=serializers.CharField()
    year=serializers.IntegerField()
    Director=serializers.CharField()
    Genre=serializers.CharField()


class MovieModelSer(serializers.ModelSerializer):
    class Meta:
        model=Movies
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)