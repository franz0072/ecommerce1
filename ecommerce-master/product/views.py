from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['PUT'])
def deactivate_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        product.deactivate_if_old()
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=404)
