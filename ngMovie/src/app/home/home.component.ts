import { Component } from '@angular/core';
import { DataService } from '../service/data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {

  movies:any;
  constructor(private ds:DataService){
    this.ds.getMovies().then(res=>res.json()).then(data=>this.movies=data)
  }

}
