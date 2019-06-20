from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class CategoryManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)

class Category(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = CategoryManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'{self.id}: {self.name}'

class ProductManager(models.Manager):
    def for_user(self, pk1, pk2, user):
        return Category.objects.for_user(user=user).get(id=pk1).task_set.get(id=pk2)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(0),
                                                                                        MaxValueValidator(10000000)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    objects = ProductManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'{self.id}: {self.name}'