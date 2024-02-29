import {Component, Input} from '@angular/core'
import { PProduct } from '../../models/products'
import { Router } from '@angular/router'

@Component ({
    selector : 'app-product',
    templateUrl : './product.component.html'
})

export class ProductComponent {
    @Input() product: PProduct

    constructor(private router: Router){}

    shareProduct(productId: number){
        this.router.navigate(['/products', productId]);
    }
    details = false
    
}