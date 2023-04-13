from django.shortcuts import render
from rest_framework.views import APIView
from .models import movies,Movies
from .serializer import Movieserializer,MovieModelSer,UserSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework import status,permissions,authentication

# Create your views here.
class Movielist(APIView):
    def get(self,req,*args,**kwargs):
        allmovies=movies
        if "Genre" in req.query_params:
            qp=req.query_params.get('Genre')
            allmovies=[i for  i in allmovies if i ['Genre']==qp]
        if "yearlt" in req.query_params:
            qp=req.query_params.get('yearlt')
            allmovies=[i for  i in allmovies if i ['yearlt']<int(qp)]
        return Response(data=allmovies)
        
    def post(self,req,*args,**kwargs):
        data=req.data
        movies.append(data)
        return Response(data=movies)


class Movie(APIView):
    def get(self,req,*args,**kwargs):
        id= kwargs.get("mid")
        film=[i for  i in movies if i ['id']==id].pop()
        return Response(data=film)

    def put(self,req,*args,**kwargs):
        id= kwargs.get("mid")
        data=req.data
        movie=[i for  i in movies if i ['id']==id].pop()
        movies.update(movie)
        return Response(data=movies)
    
    def delete(self,req,*args,**kwargs):
        id= kwargs.get("mid")
        movie=[i for  i in movies if i ['id']==id].pop()
        movies.remove(movie)
        return Response(data=movies)

class Movielist(APIView):
    def get(self,req,*args,**kwargs):
        mvs=Movies.objects.all()
        ser=Movieserializer(mvs,many=True)
        return Response(data=ser.data)
    
    def post(self,req,*args,**kwargs):
        mvs=req.data
        ser=Movieserializer(data=mvs)
        if ser.is_valid():
            name=ser.validated_data.get("name")
            yr=ser.validated_data.get("year")
            dir=ser.validated_data.get("Director")
            gen=ser.validated_data.get("Genre")
            Movies.objects.create(name=name,year=yr,Director=dir,Genre=gen)
            return Response({"Message":"Mission Success"})
        else:
            return Response({"Message":"Mission Faild!!!"})


class Movie(APIView):
    def get(self,req,*args,**kwargs):
        id = kwargs.get("mid")
        film=Movies.objects.get(id=id)
        ser=Movieserializer(film)
        return Response(data=ser.data)
    
    def delete (self ,req,*args,**kwars):
        id=kwars.get("mid")
        mv=Movies.objects.get(id=id)
        mv.delete()
        return Response({"Message":"Detelted"})

    
    def put(self,req,*args,**kwargs):
        id= kwargs.get("mid")
        mv=Movies.objects.get(id=id)
        mvdata=req.data
        ser=Movieserializer(data=mvdata)
        if ser.is_valid():
            mv.name=ser.validated_data.get("name")
            mv.year=ser.validated_data.get("year")
            mv.Director=ser.validated_data.get("Director")
            mv.Genre=ser.validated_data.get("Genre")
            mv.save()
            return Response({"Message":"Movie Detailes Updated"})
        else:
            return Response({"Message":ser.errors},status=status.HTTP_405_METHOD_NOT_ALLOWED)


# Using Model Serializer

class Films(APIView):
    def get(self,req,*args,**kwargs):
        mv=Movies.objects.all()
        Dser=MovieModelSer(mv,many=True)
        return Response (data=Dser.data)
    
    def post(self,req,*args,**kwargs):
        mvs=req.data
        ser=MovieModelSer(data=mvs)
        if ser.is_valid():
            ser.save()
            return Response({"Message":"Film Added"})
        else:
            return Response({"Message":ser.errors},status=status.HTTP_402_PAYMENT_REQUIRED)
        
    
class FilmItem(APIView):
    def get(self,req,*args,**kwargs):
        id=kwargs.get("fid")
        try:
            mv=Movies.objects.get(id=id)
            dser=MovieModelSer(mv)
            return Response (data=dser.data,)
        except:return Response({"Message":"id not found"},status=status.HTTP_404_NOT_FOUND)
    
    def delete (self ,req,*args,**kwargs):
        id=kwargs.get("fid")
        try:
            mv=Movies.objects.get(id=id)
            mv.delete()
            return Response({"Message":"Detelted"})
        except:return Response({"Message":"id not found"},status=status.HTTP_404_NOT_FOUND)

    def put(self,req,*args,**kwargs):
        id=kwargs.get("fid")
        mv=Movies.objects.get(id=id)
        ser=MovieModelSer(data=req.data,instance=mv)
        if ser.is_valid():
            ser.save()
            return Response({"Message":"Updation Success"})
        else:
            return Response({"Message":"Mission Failed"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    

class UserCreation(APIView):
    def post(self,req,*args,**kwargs):
        ser=UserSerializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response({"Message":"Registratin Completed"})
        else:
            return Response({"Message":"Registration Failed"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)

#Using Viewset Class

class MovieAPI(ViewSet):
    def list(self,req,*args,**kwargs):
        mv=Movies.objects.all()
        dser=MovieModelSer(mv,many=True)
        return Response (data=dser.data)
    def retrieve(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            mv=Movies.objects.get(id=id)
            dser=MovieModelSer(mv)
            return Response(data=dser.data)
        except:
            return Response({"Message":"Invalid ID"},status=status.HTTP_400_BAD_REQUEST)
        
    def create(self,req,*args,**kwargs):
        ser=MovieModelSer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response({"Message":"Movies Added"})
        else:
            return Response({"Message":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    def update(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        mv=Movies.objects.get(id=id)
        ser=MovieModelSer(data=req.data,instance=mv)
        if ser.is_valid():
            ser.save()
            return Response({"Message":"Movies Updated"})
        else: 
            return Response({"Message":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)      
        
    def destroy(self,req,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            Movies.objects.filter(id=id).delete()
            return Response({"msg":"Movie Deleted"})
        except:
            return Response({"Message":"Invalid ID"},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
#  Using ModelViewset
class MoviesApiMV(ModelViewSet):
    serializer_class=MovieModelSer
    queryset=Movies.objects.all()
    model=Movies
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.TokenAuthentication]