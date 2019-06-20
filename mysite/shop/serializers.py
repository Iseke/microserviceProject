from rest_framework import serializers
from users.serializers import UserSerializer
from shop.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    created_by = UserSerializer(required=False)

    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=False)

    class Meta:
        model = Product
        #exclude = ['created_at', 'updated_at']
        fields = ['id','name','price','description','available','category']

