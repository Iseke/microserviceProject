from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from shop.models import Product
from users.models import User
from order.managers import OrderManager


class Order(models.Model):
    owned_by = models.ForeignKey(User, on_delete=models.CASCADE,default=None,null=True)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    objects = OrderManager()

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return f'Order: {self.id}'

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ('quantity',)
        verbose_name = 'order item'
        verbose_name_plural = 'order items'

    def __str__(self):
        return f'OrderItem: {self.id}'

    def get_cost(self):
        return  self.product['price']*self.quantity
