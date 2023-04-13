from django.shortcuts import render
from rest_framework.views import APIView
from .models import Dishes
from rest_framework.response import Response
from .serializer import Dishserializer,DishModelSer,UserSerializer
from rest_framework import status


class Dishlist(APIView):
    def get(self,req,*args,**kwargs):
        mvs=Dishes.objects.all()
        ser=Dishserializer(mvs,many=True)
        return Response(data=ser.data)


class Dish(APIView):
    def get(self,req,*args,**kwargs):
        id= kwargs.get("mid")
        film=[i for  i in Dishes if i ['id']==id].pop()
        return Response(data=film)

    def put(self,req,*args,**kwargs):
        id= kwargs.get("mid")
        data=req.data
        movie=[i for  i in Dishes if i ['id']==id].pop()
        Dishes.update(movie)
        return Response(data=Dishes)
    
    def delete(self,req,*args,**kwargs):
        id= kwargs.get("mid")
        movie=[i for  i in Dishes if i ['id']==id].pop()
        Dishes.remove(movie)
        return Response(data=Dishes)

#Serializer

class Dishlist(APIView):
    def get(self,req,*args,**kwargs):
        mvs=Dishes.objects.all()
        ser=Dishserializer(mvs,many=True)
        return Response(data=ser.data)
    
    def post(self,req,*args,**kwargs):
        mvs=req.data
        ser=Dishserializer(data=mvs)
        if ser.is_valid():
            name=ser.validated_data.get("name")
            pr=ser.validated_data.get("price")
            cat=ser.validated_data.get("category")
            Dishes.objects.create(name=name,price=pr,category=cat)
            return Response({"Message":"Mission Success"})
        else:
            return Response({"Message":"Mission Faild!!!"})


class Dish(APIView):
    def get(self,req,*args,**kwargs):
        id = kwargs.get("mid")
        film=Dishes.objects.get(id=id)
        ser=Dishserializer(film)
        return Response(data=ser.data)
    
    def delete (self ,req,*args,**kwars):
        id=kwars.get("mid")
        mv=Dishes.objects.get(id=id)
        mv.delete()
        return Response({"Message":"Detelted"})

    
    def put(self,req,*args,**kwargs):
        id= kwargs.get("mid")
        mv=Dishes.objects.get(id=id)
        mvdata=req.data
        ser=Dishserializer(data=mvdata)
        if ser.is_valid():
            mv.name=ser.validated_data.get("name")
            mv.price=ser.validated_data.get("price")
            mv.category=ser.validated_data.get("category")
            mv.save()
            return Response({"Message":"Movie Detailes Updated"})
        else:
            return Response({"Message":ser.errors},status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Using Model Serializer

class Dishes(APIView):
    def get(self,req,*args,**kwargs):
        mv=Dishes.objects.all()
        Dser=DishModelSer(mv,many=True)
        return Response (data=Dser.data)
    
    def post(self,req,*args,**kwargs):
        mvs=req.data
        ser=DishModelSer(data=mvs)
        if ser.is_valid():
            ser.save()
            return Response({"Message":"Film Added"})
        else:
            return Response({"Message":ser.errors},status=status.HTTP_402_PAYMENT_REQUIRED)
        
    
class DishItem(APIView):
    def get(self,req,*args,**kwargs):
        id=kwargs.get("fid")
        try:
            mv=Dishes.objects.get(id=id)
            dser=DishModelSer(mv)
            return Response (data=dser.data,)
        except:return Response({"Message":"id not found"},status=status.HTTP_404_NOT_FOUND)
    
    def delete (self ,req,*args,**kwargs):
        id=kwargs.get("fid")
        try:
            mv=Dishes.objects.get(id=id)
            mv.delete()
            return Response({"Message":"Detelted"})
        except:return Response({"Message":"id not found"},status=status.HTTP_404_NOT_FOUND)

    def put(self,req,*args,**kwargs):
        id=kwargs.get("fid")
        mv=Dishes.objects.get(id=id)
        ser=DishModelSer(data=req.data,instance=mv)
        if ser.is_valid():
            ser.save()
            return Response({"Message":"Updation Success"})
        else:
            return Response({"Message":"Mission Failed"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
#UserCreations 

class UserCreation(APIView):
    def post(self,req,*args,**kwargs):
        ser=UserSerializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response({"Message":"Registratin Completed"})
        else:
            return Response({"Message":"Registration Failed"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
