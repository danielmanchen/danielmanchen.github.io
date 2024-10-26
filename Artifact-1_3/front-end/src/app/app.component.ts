//app.component.ts

import { Component, OnInit,ViewChild} from '@angular/core';
import { ApiService } from './api.service';
import { data } from 'jquery';


@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})



export class AppComponent implements OnInit {
    
    
    title = 'Grocer Inventory Appication';
    displayedColumns: string[] = ['itemName', 'quantity'];
    message: any;
    showAddNew = false;
    quantity: any;
    constructor(private ApiService: ApiService) { };
    selectedRadio: string='';

    
    ngOnInit() {
        this.ApiService.getInventory().subscribe(data => {
            this.message = data;  
        });
        
    }
    addNew(){
        this.showAddNew = !this.showAddNew;
   }
   decrease(event: any): void{
    this.quantity = event.target.value--;
    console.log(event.target.name); 
    this.ApiService.updateItem(event.target.name, this.quantity)
    .subscribe(
        () => {
            console.log(event.target.name + ' is now ' + this.quantity);
        },
        (error) => {
            console.log('could not update quantity');
        }
    )
    
   }
   increase(event: any){
    event.target.value++;
    console.log(event.target.value);
   }
   delete(): void{
    console.log(this.selectedRadio);
    this.ApiService.deleteItem(this.selectedRadio)
    .subscribe(
        () => {
            console.log('Item deleted');
        },
        (error) => {
            console.log('Error deleting ', error);
        }
    )
    window.location.reload();
    
   }
   
   
}
