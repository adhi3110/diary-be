from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated  # <-- Here


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        name = request.data['name']
        if name:
            return Response({'name': name})
        else:
            return Response({'hell': name})
