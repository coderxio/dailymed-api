from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dailymed import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'set', views.SetViewSet)
router.register(r'spl', views.SplViewSet)
router.register(r'ndc', views.NdcViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]