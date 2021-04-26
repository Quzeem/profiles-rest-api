from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
  """APIView Demo"""

  def get(self, request, format=None):
    """Returns a list of some APIView features"""
    an_apiview = [
      'Uses HTTP methods(GET, POST, PUT, PATCH, DELETE) as functions',
      'Is similar to a traditional Django view',
      'Gives us full control over our application logic',
      'Is manually mapped to URLs'
    ]

    return Response({ 'message': 'Hello there!', 'an_apiview': an_apiview })
