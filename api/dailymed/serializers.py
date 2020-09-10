from rest_framework import serializers
from dailymed.models import Set, Spl, Product, Package


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'


class SplSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spl
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
