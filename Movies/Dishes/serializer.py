from rest_framework import serializers

class Dishserializer(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.IntegerField()
    category=serializers.CharField()