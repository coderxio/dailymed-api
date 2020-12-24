from rest_framework import viewsets, mixins
from dailymed.models import Set, Spl, Product, Package, RxNorm
from dailymed.serializers import (
    SetSerializer,
    SplSerializer,
    ProductSerializer,
    PackageSerializer,
    RxNormSerializer,
    SuperSerializer
)
from dailymed.filters import SplFilter, SuperFilter


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
    filterset_class = SplFilter


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


class RxNormViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = RxNorm.objects.all()
    serializer_class = RxNormSerializer


class SuperViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Set.objects.all()
    serializer_class = SuperSerializer
    filterset_class = SuperFilter
