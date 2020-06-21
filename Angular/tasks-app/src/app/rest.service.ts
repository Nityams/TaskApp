import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http';
import { Observable, throwError as observableThrowError } from 'rxjs';
import { ITask } from './model/taskModel';


const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json',
  })
};

@Injectable({
  providedIn: 'root'
})


export class RestService {
  restUrl = 'http://127.0.0.1:5000/';

  constructor(private http: HttpClient) { }

  retriveTasks():Observable<any>{
    return this.http.get(this.restUrl,httpOptions);
  }

  deleteTasks(id){
    return this.http.get(this.restUrl+'delete/'+id,httpOptions);
  }

  addTasks(content){
    return this.http.post(this.restUrl,
      JSON.stringify({'content':content}),
      httpOptions);
  } 


  errorHandler(error: HttpErrorResponse) {
    console.log(error.message);
    console.log(error.statusText);
    console.log(error.error);
    console.log(error.ok);
    console.log(error.status);
    console.log(error.url);
    console.log(error.type);
    return observableThrowError(error.message || 'Server Error');
  }
  
}
