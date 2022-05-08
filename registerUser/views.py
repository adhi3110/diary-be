from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
import time


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        name = request.data['name']
        if name:
            return Response({'name': name})
        else:
            return Response({'hell': name})


@api_view(['POST', 'GET'])
def trial(request):
    time.sleep(6)
    print(request.data)
    return Response({})
