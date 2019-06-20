export interface IUser {
  id: number;
  username: string;
  email: string;
}
export interface IProduct {
  id: number;
  category: ICategory;
  name: string;
  description: Text;
  price: number;
  created_at: Date;
  updated_at: Date;
  available: boolean;
}
export interface ICategory {
  id: number;
  name: string;
}
export interface IAuthResponse {
  token: string;
}
export interface IOrderItem {
  id: number;
  order: IOrder;
  product: IProduct;
  quantity: number;
}
export interface IOrder {
  id: number;
  owned_by: IUser;
  address: string;
  postal_code: string;
  city: string;
  paid: boolean;
  discount: number;
}
