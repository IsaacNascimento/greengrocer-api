from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def index(request):
    data = [
        {"message": "Hello! You are at Api's app index"},
        {"data": [
            {"Auth"},
            {"Products": [
                {"categories": "get-category-list"},
            ],
            },
            {"Cart"},
            {"Orders"},
        ],
        },
    ]
    return Response(data)


