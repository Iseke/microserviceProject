from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.decorators import permission_classes
from order.serializers import OrderSerializer, OrderItemSerializer
from order.models import Order, OrderItem


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # def get_queryset(self):
    #     return Order.objects.for_user(self.request.user)

    def perform_create(self, serializer):
        serializer.save(owned_by=self.request.user)


class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    # def get_queryset(self):
    #     return Order.objects.for_user(self.request.user)


class OrderItemList(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    pagination_class = PageNumberPagination
    pagination_class.page_size = 8

    # def get_queryset(self):
    #     order = get_object_or_404(Order, id=self.kwargs[self.lookup_field], owned_by=self.request.user)
    #     return OrderItem.objects.filter(order=order)

    def perform_create(self, serializer):
        order = get_object_or_404(Order, id=self.kwargs[self.lookup_field])
        serializer.save(order=order)

