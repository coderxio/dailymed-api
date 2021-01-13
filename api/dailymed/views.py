from rest_framework import viewsets, mixins
from dailymed.models import Set, Spl, Product, Package, RxNorm
from dailymed.serializers import (
    SetSerializer,
    SplSerializer,
    ProductSerializer,
    PackageSerializer,
    RxNormSerializer,
    DetailSerializer
)
from dailymed.filters import SplFilter, SetFilter


class DualSetSerializerViewSet(viewsets.ModelViewSet):
    """
    ViewSet providing different serializers for list and detail views.

    Use list_serializer and detail_serializer to provide them
    """
    def list(self, *args, **kwargs):
        self.serializer_class = SetSerializer
        self.filterset_class = SetFilter
        return viewsets.ModelViewSet.list(self, *args, **kwargs)

    def retrieve(self, *args, **kwargs):
        self.serializer_class = DetailSerializer
        return viewsets.ModelViewSet.retrieve(self, *args, **kwargs)


class SetViewSet(DualSetSerializerViewSet):

    queryset = Set.objects.all()
    list_serializer = SetSerializer
    retrieve_serializer = DetailSerializer


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
