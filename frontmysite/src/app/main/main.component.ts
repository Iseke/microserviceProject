import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../shared/services/provider.service';
import {ICategory, IOrder, IOrderItem, IProduct} from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public categories: ICategory[] = [];
  public products: IProduct[] = [];
  public  orders: IOrder[] = [];
  public items: IOrderItem[] = [];
  public targetCategory: ICategory;
  public targetOrder: IOrder;
  public CatName = '';
  public ProdName = '';
  public username = '';
  public password = '';
  public logged = false;
  public searchProduct = '';
  public description = '';
  public price = 0;
  public count = 0;
  public available = false;
  public address = '';
  public postalcode = '';
  public city = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if ( token ) {
      this.logged = true;
    }

    if (this.logged) {
      this.provider.getCategories().then(res => {
        this.categories = res;
      });
    }
  }
  getProductList(category: ICategory) {
    this.provider.getProduct(category.id).then(res => {
      this.targetCategory = category;
      this.products = res;
    });
  }
  createCat() {
    if (this.CatName !== '') {
      this.provider.createCategory(this.CatName).then(res => {
        this.CatName = '';
        this.categories.push(res);
      });
    }
  }
  updateCat(category: ICategory) {
    this.provider.updateCategory(category).then(res => {});
  }
  deleteCat(category: ICategory) {
    this.provider.deleteCategory(category).then( res => {
      this.provider.getCategories().then( re => {
        this.categories = re;
      });
    });
  }
  createProd() {
    if (this.targetCategory !== undefined) {
      this.provider.createProduct(this.ProdName, this.price, this.description, this.available, this.targetCategory).then(res => {
        this.ProdName = '';
        this.price = 0;
        this.description = '';
        this.available = false;
        this.provider.getProduct(this.targetCategory.id).then(re => {
          this.products = re;
        });
      });
    } else  {
      alert('Click to the taskList where you would like to add task!');
    }

  }
  updateProd(product: IProduct) {
    this.provider.updateProduct(product).then(res => {});
  }
  deleteProd(product: IProduct) {
    this.provider.deleteProduct(product).then( res => {
      this.provider.getProduct(product.category.id).then( re => {
        this.products = re;
      });
    });
  }

  searchProd() {
    if (this.targetCategory === undefined) {
      alert('Click to the taskList to see tasks');
    } else {
      this.provider.getProduct(this.targetCategory.id, this.searchProduct).then(res => {
          this.products = res;
        });
    }
  }
  getOrdr() {
    this.provider.getOrders().then(res => {
      this.orders = res;
    });
  }
  createOrdr() {
    this.provider.createOrders(this.address, this.postalcode, this.city).then(res => {
      this.address = '';
      this.postalcode = '';
      this.city = '';
      this.provider.getOrders().then(re => {
        this.orders = re;
      });
    });
  }
  updateOrdr(order: IOrder) {
    this.provider.updateOrder(order).then(res => {});
  }
  deleteOrdr(order: IOrder) {
    this.provider.deleteOrder(order).then(res => {
      this.provider.getOrders().then(re => {
        this.orders = re;
      });
    });
  }
  getItm(order: IOrder) {
    this.provider.getItems(order.id).then(res => {
      this.items = res;
      this.targetOrder = order;
    });
  }
  createItm() {
    this.provider.createItem(this.ProdName, this.count, this.targetOrder).then(res => {
      this.ProdName = '';
      this.count = 0;
      this.provider.getItems(this.targetOrder.id).then(re => {
        this.items = re;
      });
    });
  }
  deleteItm(item: IOrderItem) {
    this.provider.deleteItem(item).then(res => {
      this.provider.getItems(item.order.id).then(re => {
        this.items = re;
      });
    });
  }
  login() {
    if (this.username !== '' && this.password !== '') {
      this.provider.login(this.username, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.logged = true;
        this.provider.getCategories().then(r => {
          this.categories = r;
        });
      });
    }
  }
  logout() {
    this.provider.logout().then(res => {
      localStorage.clear();
      this.username = '';
      this.password = '';
      this.logged = false;
    });
  }

}
