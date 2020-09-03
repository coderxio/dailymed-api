from dailymed.models import Set, Spl, Ndc
from dailymed.serializers import SetSerializer, SplSerializer, NdcSerializer
from rest_framework import permissions, viewsets, mixins

# Create your views here.
class SetViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer

class SplViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Spl.objects.all()
    serializer_class = SplSerializer

class NdcViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Ndc.objects.all()
    serializer_class = NdcSerializer
    lookup_field = 'ndc'