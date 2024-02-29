import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { PProduct } from './models/products';
import { products as data} from './data/products';
@Component({
  selector: 'app-root',
  standalone: false,
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'my app';
  term: ''
  products: PProduct[] = data
}
