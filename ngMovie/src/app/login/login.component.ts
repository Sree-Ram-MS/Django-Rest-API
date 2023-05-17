import { Component } from '@angular/core';
import { FormBuilder,Validators } from '@angular/forms';
import { DataService } from '../service/data.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  logform=this.fb.group({
    username:['',[Validators.required,Validators.pattern("[a-zA-Z 0-9]+")]],
    password:['',[Validators.required,Validators.minLength(2)]]
  })

  constructor(private fb:FormBuilder,private ds:DataService,private rt:Router){}

  clicked(){
    // alert(this.logform.value.username)
    this.ds.login(this.logform.value).then(res=>res.json()).then(data=>{
      console.log(data)
      if(data["token"]){
        localStorage.setItem('token',data['token'])
        this.rt.navigate(['home'])
        alert("Login Success")
      }
      else{
        alert("invalid Username or Password")
      }
    })
  }

}
