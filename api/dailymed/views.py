from rest_framework import viewsets, mixins
from dailymed.models import Set, Spl, Product, Package
from dailymed.serializers import (
    SetSerializer,
    SplSerializer,
    ProductSerializer,
    PackageSerializer,
)


class SetViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


class SplViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Spl.objects.all()
    serializer_class = SplSerializer


class ProductViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PackageViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
