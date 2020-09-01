from rest_framework import serializers
from dailymed.models import Set, Spl, Ndc

class SetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Set
        fields = ['id', 'name', 'spls']
        extra_kwargs = {
            'spls': {'lookup_field': 'name'}
        }

class SplSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spl
        fields = ['id', 'name', 'set', 'ndcs']
        extra_kwargs = {
            'set': {'lookup_field': 'name'},
            'ndcs': {'lookup_field': 'value'}
        }

class NdcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ndc
        fields = ['id', 'value', 'spl']
        extra_kwargs = {
            'spl': {'lookup_field': 'name'},
        }