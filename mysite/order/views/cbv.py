from order.models import OrderItem,Order
from order.serializers import OrderSerializer,OrderItemSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class OrderItemDetail(APIView):

    def get_item(self, request, pk1, pk2):
        try:
            items = Order.objects.get(id=pk1).items.get(id=pk2)
        except:
            raise Http404
        return items

    def get(self, request, pk1, pk2):
        item = self.get_item(request, pk1, pk2)
        serializer = OrderItemSerializer(item)
        return Response(serializer.data)


    def delete(self, request, pk1, pk2):
        item = self.get_item(request, pk1, pk2)
        item.delete()
        return Response({"delete_status": "successful"})