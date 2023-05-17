import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor() { }

  login(data:any){
    return fetch('http://127.0.0.1:8000/token-auth/', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
    })
  }

  getMovies(){
    return fetch('http://127.0.0.1:8000/MVapi/', {
      method: 'GET',
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
        'Authorization': `Token ${localStorage.getItem("token")}`
      },
    })
  }


}
