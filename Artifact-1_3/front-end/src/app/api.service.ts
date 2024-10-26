//api.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class ApiService {
    constructor(private http: HttpClient) { }
    getInventory() {
        return this.http.get(
            'http://localhost:3000/api/inventory');
    }
    deleteItem(name: string) {
        return this.http.delete(
            'http://localhost:3000/api/inventory/' + name); 
              
    }
    createItem() {
        return this.http.post(
            'http://localhost:3000/api/inventory', {'quantity' : 1} );
        
    }
    updateItem(name: string, quantity: number) {
        return this.http.put(
          'http://localhost:3000/api/inventory/' + name, quantity  
        );
    }
}