from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
# We only need to specify the base_name if we are creating a viewset that doesn't have a queryset or if we want to override the name of the queryset assosciated to it
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profiles', views.UserViewSet)
router.register('feeds', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view', views.HelloApiView.as_view()),  # APIView
    path('login', views.UserLoginApiView.as_view()),
    # ViewSet - The API URL Configurations are automatically generated by the router
    path('', include(router.urls))
]
