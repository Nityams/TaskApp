import { Component, OnInit } from '@angular/core';
import { RestService } from '../rest.service';
import { ITask } from '../model/taskModel';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  
  public todo: String;
  public tasks : ITask[];
  public todoTask : String;

  constructor(private _restService: RestService) {

   }

  addToDo(todoString: String){
    this.todoTask = '';
    this._restService.addTasks(todoString)
    .subscribe(data => {
      this.tasks = data['task_list'];
    },
    error => console.log(error));
  }

  delete(task: String){
    this._restService.deleteTasks(task)
    .subscribe(data=>{
      this.tasks = data['task_list']
    },
    error => console.log(error));
  }

  ngOnInit() {
    this._restService.retriveTasks()
    .subscribe(data => {
      this.tasks = data['task_list']
    },
    error => console.log(error));
  }

}
