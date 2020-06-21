import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {APP_BASE_HREF} from '@angular/common';
import {MainComponent} from './main/main.component';

const routes: Routes = [
  {
    path: 'app',
    pathMatch: 'full',
    component: MainComponent
  },
  {
    path:'**',
    redirectTo:"app"
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [{provide: APP_BASE_HREF, useValue : '/' }]
})
export class AppRoutingModule { }
