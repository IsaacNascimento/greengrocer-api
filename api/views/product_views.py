from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Category
from rest_framework import status
from api.serializers.product_serializer import CategorySerializer

@api_view(['GET'])
def get_category_list(request):
     categories = Category.objects.all()
     serializer = CategorySerializer(categories, many=True)
     data = {"result": serializer.data}
     return Response(data, status=status.HTTP_200_OK)



