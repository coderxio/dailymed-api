from rest_framework import serializers
from dailymed.models import Set, Spl, Product, InactiveIngredient, Package


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        exclude = ('product', )


class InactiveIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = InactiveIngredient
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True)
    inactive_ingredients = InactiveIngredientSerializer(many=True)

    class Meta:
        model = Product
        exclude = ('spl', )


class SplSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Spl
        fields = '__all__'


class SetSerializer(serializers.ModelSerializer):
    spls = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='spl-detail',
    )

    class Meta:
        model = Set
        fields = '__all__'
