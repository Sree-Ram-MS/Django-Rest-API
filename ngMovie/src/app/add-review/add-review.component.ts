import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from '../service/data.service';

@Component({
  selector: 'app-add-review',
  templateUrl: './add-review.component.html',
  styleUrls: ['./add-review.component.css']
})
export class AddReviewComponent {

  rid:any;
  revForm=this.fm.group({
    review:'',
    rating:''
  })

  constructor(private fm:FormBuilder,private at:ActivatedRoute,private ds:DataService,private rt:Router){
    at.params.subscribe((data:any)=>this.rid=data["id"])
  }

  comment(){
    this.ds.PushReviews(this.rid,this.revForm.value).then(res=>res.json()).then((data:any)=>{
      if(data['msg']=="Added"){
        alert("Review Added")
        this.rt.navigate(['home'])
      }
      else{
        alert(" Something Went Wrong!!")
      }
    })
  }

}
