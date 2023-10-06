from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Category, Product
from rest_framework import status
from api.serializers.product_serializer import CategorySerializer, ProductSerializer

@api_view(['GET'])
def get_category_list(request):
     categories = Category.objects.all()
     serializer = CategorySerializer(categories, many=True)
     data = {"result": serializer.data}
     return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product_list(request):
     products = Product.objects.select_related('category')
     serializer = ProductSerializer(products, many=True)
     data = {"result": serializer.data}
     # print(data)
     return Response(data, status=status.HTTP_200_OK)



