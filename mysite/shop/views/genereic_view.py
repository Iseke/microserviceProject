from django.http import Http404
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes

from shop.serializers import CategorySerializer, ProductSerializer
from shop.models import Category, Product
from shop.filters import ProductFilter


class CategoryList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return Category.objects.for_user(user=self.request.user)

class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    pagination_class = PageNumberPagination
    pagination_class.page_size = 4

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)

    filter_class = ProductFilter
    search_fields = ('name',)
    ordering_fields = ('name', 'price')

    def get_queryset(self):
        category = get_object_or_404(Category, id=self.kwargs[self.lookup_field])
        return Product.objects.filter(category=category,)

    def perform_create(self, serializer):
        try:
            category = Category.objects.get(id=self.kwargs['pk'])
        except Category.DoesNotExist:
            raise Http404
        serializer.save(category=category)


