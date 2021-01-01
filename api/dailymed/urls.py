from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dailymed import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'api/v1/set', views.SetViewSet)
router.register(r'api/v1/spl', views.SplViewSet)
router.register(r'api/v1/product', views.ProductViewSet)
router.register(r'api/v1/ndc', views.PackageViewSet)
router.register(r'api/v1/rxnorm', views.RxNormViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
