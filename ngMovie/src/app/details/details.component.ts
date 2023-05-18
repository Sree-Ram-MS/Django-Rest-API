import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DataService } from '../service/data.service';

@Component({
  selector: 'app-details',
  templateUrl: './details.component.html',
  styleUrls: ['./details.component.css']
})
export class DetailsComponent {

  
  film:any;
  rev:any;

  constructor(private ar:ActivatedRoute,private ds:DataService){
    this.ar.params.subscribe((res:any)=>{
    // this.film=res["id"]
    
      this.film=this.ds.fetchFilms(res.id).then(res=>res.json()).then((data:any)=>{this.film=data})
      console.log(this.film)
      this.rev=this.ds.fetchReviews(res.id).then(res=>res.json()).then((data:any)=>{this.rev=data;console.log(data)})
    }
    )
    // console.log(this.film)
    // this.ds.fetchFilms(this.film).then(data=>data.json()).then((res:any)=>console.log(res))
    
  }

}
