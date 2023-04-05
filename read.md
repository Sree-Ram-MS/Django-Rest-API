API PLANNING:

1.To get all movie list 
        url:127.0.0.1:8000/movies
        Method:GET
        response:movie list

2.To get specific movie details
        url:127.0.0.1:8000/movies/1
        Method:GET
        response:a specifi movie

3.to add a new movie
        url:127.0.0.1:8000/movies
        method:POST
        data:{
                "name":"Dada",


        }

4. To Update a specific movie detailes:
        url:127.0.0.1:8000/movies/1
        Method:PUT
        data:{"id":1,"name":"Dada","year":2023,"Director":"Ganesh","Genre":"Feel Good"}
        response:complete list

5. to delete a specific movie
        url:127.0.0.1:8000/movies/1
        Method:DELETE
        response:complete list

6. to get list 








