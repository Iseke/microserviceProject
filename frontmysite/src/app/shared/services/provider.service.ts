import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient, HttpClientModule} from '@angular/common/http';
import {IAuthResponse, ICategory, IOrder, IOrderItem, IProduct, IUser} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }
  getUsers(): Promise <IUser[]> {
    return this.get('http://localhost:8000/api/users/', {});
  }
  updateUser(user: IUser) {
    return this.put(`http://localhost:8000/api/users/${user.id}/`, {
      username: user.username
    });
  }
  deleteUser(user: IUser) {
    return this.del(`http://localhost:8000/api/users/${user.id}/`, {});
  }
  login(login: any, passwd: any): Promise < IAuthResponse > {
    return this.post('http://127.0.0.1:8000/api/login/', {
      username: login,
      password: passwd
    });
  }
  logout(): Promise < any > {
    return this.post('http://127.0.0.1:8000/api/logout/', {});
  }
  getCategories(): Promise <ICategory[]> {
    return  this.get('http://127.0.0.1:8000/api/shop/categories/', {});
  }
  getProduct(id: number, search = ''): Promise <IProduct[]> {
    return this.get(`http://127.0.0.1:8000/api/shop/categories/${id}/products/?` + 'name=' + search, {});
  }
  createCategory(nm: string): Promise <ICategory> {
    return  this.post('http://127.0.0.1:8000/api/shop/categories/', {
      name: nm
    });
  }
  updateCategory(category: ICategory) {
    return  this.put(`http://127.0.0.1:8000/api/shop/categories/${category.id}/`, {
      name: category.name
    });
  }
  deleteCategory(category: ICategory) {
    return this.del(`http://127.0.0.1:8000/api/shop/categories/${category.id}/`, {});
  }
  updateProduct(product: IProduct) {
    return this.put(`http://127.0.0.1:8000/api/shop/categories/${product.category.id}/products/${product.id}`, {
      name: product.name ,
      price: product.price,
      description: product.description
    });
  }
  createProduct(nme: string, pric: number, descrp: string, avail: boolean, category: ICategory) {
    return this.post(`http://127.0.0.1:8000/api/shop/categories/${category.id}/products/`, {
      name: nme,
      price: pric,
      description: descrp,
      available: avail
    });
  }
  deleteProduct(product: IProduct) {
    return this.del(`http://127.0.0.1:8000/api/shop/categories/${product.category.id}/products/${product.id}`, {});
  }
  getOrders(): Promise <IOrder[]> {
    return this.get(`http://127.0.0.1:8000/api/order/orders/`, {});
  }
  createOrders(addr: string, postcode: string, cit: string): Promise <IOrder> {
    return this.post(`http://127.0.0.1:8000/api/order/orders/`, {
      address: addr,
      postal_code: postcode,
      city: cit
    });
  }
  updateOrder(order: IOrder) {
    return this.put(`http://127.0.0.1:8000/api/order/orders/${order.id}/`, {
      address: order.address,
      postal_code: order.postal_code,
      city: order.city
    });
  }
  deleteOrder(order: IOrder) {
    return this.del(`http://127.0.0.1:8000/api/order/orders/${order.id}/`, {});
  }
  getItems(id: number): Promise <IOrderItem[]> {
    return this.get(`http://127.0.0.1:8000/api/order/orders/${id}/items/`, {});
  }
  // updateItems(items: IOrderItem) {
  //   return this.put(`http://127.0.0.1:8000/api/order/orders/${order.id}/`, {
  //
  //   });
  // }
  createItem(prod: string, count: number, order: IOrder): Promise <IOrderItem> {
    return this.post(`http://127.0.0.1:8000/api/order/orders/${order.id}/items/`, {
      product: prod,
      quantity: count
    });
  }
  deleteItem(item: IOrderItem) {
    return this.del(`http://127.0.0.1:8000/api/order/orders/${item.order.id}/items/${item.id}/`, {});
  }
}
