from django.shortcuts import render
from rest_framework.views import APIView
from .models import dishes,Dishes
from rest_framework.response import Response
from .serializer import Dishserializer


# Create your views here.
# class Dishlist(APIView):
#     def get(self,req,*args,**kwargs):
#         alldishes=dishes
#         if "price" in req.query_params:
#             qp=req.query_params.get('price')
#             alldishes=[i for i in alldishes if i ['price']<int(qp)]
#         if "Category" in req.query_params:
#             qp=req.query_params.get('Category')
#             alldishes=[i for i in alldishes if i ['Category']==qp]
#         return Response(data=alldishes)

#     def post(self,req,*args,**kwargs):
#         data=req.data
#         dishes.append(data)
#         return Response(data=dishes)
        
    
# class Dish(APIView):
#     def get(self,req,*args,**kwargs):
#         id= kwargs.get("did")
#         dish=[i for i in dishes if i ['id']==id].pop()
#         return Response(data=dish)

#     def put(self,req,*args,**kwargs):
#         id= kwargs.get("did")
#         dish=req.data
#         dish=[i for  i in dishes if i ['id']==id].pop()
#         dishes.update(dish)
#         return Response(data=dishes)

#     def delete(self,req,*args,**kwargs):
#         id= kwargs.get("did")
#         dish=[i for  i in dishes if i ['id']==id].pop()
#         dishes.remove(dish)
#         return Response(data=dishes)


class Dishlist(APIView):
    def get(self,req,*args,**kwargs):
        mvs=Dishes.objects.all()
        ser=Dishserializer(mvs,many=True)
        return Response(data=ser.data)