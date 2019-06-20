from users.models import UserProfile
from shop.models import Category,Product
from shop.serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_product(self, request, pk1, pk2):
        try:
            product = Category.objects.for_user(user=request.user).get(id=pk1).product.get(id=pk2)
        except:
            raise Http404
        return product

    def get(self, request, pk1, pk2):
        product1 = self.get_product(request, pk1, pk2)
        serializer = ProductSerializer(product1)
        return Response(serializer.data)

    def put(self, request, pk1, pk2):
        product = self.get_product(request, pk1, pk2)
        try:
            request.data.pop('category')
        except:
            pass
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk1, pk2):
        product = self.get_product(request, pk1, pk2)
        product.delete()
        return Response({"delete_status": "successful"})