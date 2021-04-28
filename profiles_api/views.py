from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from . import serializers
from .models import User, UserProfileFeed
from .permissions import UpdateOwnProfile, UpdateOwnFeed


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


# We need to define the action implementations explicitly - ViewSet does not provide any implementations of actions(list, retrieve...)
class HelloViewSet(viewsets.ViewSet):
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


# Includes implementations for various actions by default. As with ModelViewSet, we'll need to provide at least the queryset and serializer_class attributes
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'retrieve', 'create', 'update', 'partial_update', and 'destroy' actions
    """
    # queryset represent a collection of objects from our database. It can have zero, one or many filters.
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (SearchFilter,)
    # Allows us to search for objects by name or email field
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creation of user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'retrieve', 'create', 'update', 'partial_update', and 'destroy' actions
    """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserProfileFeedSerializer
    queryset = UserProfileFeed.objects.all()
    permission_classes = (UpdateOwnFeed, IsAuthenticated,)

    # Allows us to customize the behaviour for creating objects through ModelViewSet
    def perform_create(self, serializer):
        """Sets the 'user' field to the logged in user"""
        serializer.save(user=self.request.user)
