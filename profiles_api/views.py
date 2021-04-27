from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

from . import serializers


class HelloApiView(APIView):
    """APIView Demo"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of some APIView features"""
        an_apiview = [
            'Uses HTTP methods(GET, POST, PUT, PATCH, DELETE) as functions',
            'Is similar to a traditional Django view',
            'Gives us full control over our application logic',
            'Is manually mapped to URLs'
        ]

        return Response({'message': 'Hello there!', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        """Create a hello message with a name input"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle an object update"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle an object partial update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(ViewSet):
    """ViewSet Demo"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Returns some ViewSet features"""
        a_viewset = [
            'Uses actions(list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello there!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a hello message with a name input"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve an object by its ID"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Handle an object update"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle an object partial update"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
