import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-add-new-item',
  templateUrl: './add-new-item.component.html',
  styleUrl: './add-new-item.component.css',
  
})
export class AddNewItemComponent {
  @Input() title = 'Add New Item';
}
