from django_filters import rest_framework as filters
from dailymed.models import Spl

class SplFilter(filters.FilterSet):
    set_id = filters.CharFilter(field_name='set__id', lookup_expr='iexact')
    labeler = filters.CharFilter(field_name='labeler', lookup_expr='icontains')
    package_ndc = filters.CharFilter(field_name='products__packages__code', lookup_expr='icontains')
    product_ndc = filters.CharFilter(field_name='products__code', lookup_expr='icontains')
    product_name = filters.CharFilter(field_name='products__name', lookup_expr='icontains')
    inactive_ingredient_name = filters.CharFilter(field_name='products__inactive_ingredients__name', lookup_expr='icontains')
    inactive_ingredient_unii = filters.CharFilter(field_name='products__inactive_ingredients__unii', lookup_expr='icontains')
    schedule = filters.CharFilter(field_name='products__schedule', lookup_expr='iexact')

    class Meta:
        model = Spl
        fields = []
