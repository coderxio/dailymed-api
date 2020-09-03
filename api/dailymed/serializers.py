from rest_framework import serializers
from dailymed.models import Set, Spl, Ndc

class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        fields = ['id', 'spls']

class SplSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spl
        fields = ['id', 'set', 'ndcs']
        extra_kwargs = {
            'ndcs': {'lookup_field': 'ndc'}
        }

class NdcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ndc
        fields = ['id', 'ndc', 'spl']