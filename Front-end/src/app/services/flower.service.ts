import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { baseURL } from '../shared/baseURL';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FlowerService {

  constructor(private http: HttpClient,) {
   }

   getFlowerCode(input : any) : Observable<any> {
     console.log(input);
     let inputData =  {
       "sepal_length" : input[0],
       "sepal_width" : input[1],
       "petal_length" : input[2],
       "petal_width" : input[3]
     }
     return this.http.post(`${baseURL}/calculate-score`, inputData);
   }
}
