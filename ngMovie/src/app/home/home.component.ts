import { Component } from '@angular/core';
import { DataService } from '../service/data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  movies:any;
  constructor(private ds:DataService,private rt:Router){
    this.ds.getMovies().then(res=>res.json()).then(data=>this.movies=data)
  }

  details(ev:any){
    this.rt.navigate(['ViewMore',ev.target.id])
  }

  addrev(e:any){
    this.rt.navigate(['addreview',e.target.id])
  }

  logout(){
    localStorage.removeItem('token')
    this.rt.navigate([''])
  }
}
