import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-grid',
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css']
})
export class GridComponent implements OnInit {
  areas: any[] = new Array(9);
  solution: any;
  iterator: any[] = [0, 1, 2];
  gotSolution = false;

  constructor(private http: HttpClient) {
    for ( let i = 0 ; i <= 8; i++) {
      this.areas[i] = new Array(9);
      }
    for ( let i = 0 ; i <= 8; i++) {
      for ( let j = 0 ; j <= 8; j++) {
        this.areas[i][j] = '';
        }
        }
    console.log(this.areas);
   }

  ngOnInit() {
  }

  private SubmitData() {
      this.http.post('http://127.0.0.1:5000/solution', {data: this.areas}).subscribe(posts => {
      console.log(posts);
      this.solution = posts[0];
      this.gotSolution = true;
      this.areas = this.solution;
    });
  }

  private ResetData() {
    for ( let i = 0 ; i <= 8; i++) {
      for ( let j = 0 ; j <= 8; j++) {
        this.areas[i][j] = '';
        }
        }
  }
}
