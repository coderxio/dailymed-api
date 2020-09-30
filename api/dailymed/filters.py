from django_filters import rest_framework as filters
from dailymed.models import Spl


SCHEDULE_CHOICES = (
    ('', ''),
    ('CII', 'CII'),
    ('CIII', 'CIII'),
    ('CIV', 'CIV'),
    ('CV', 'CV')
)


class SplFilter(filters.FilterSet):
    set_id = filters.CharFilter(
        field_name='set__id',
        lookup_expr='iexact',
        distinct=True)
    labeler = filters.CharFilter(
        field_name='labeler',
        lookup_expr='icontains',
        distinct=True)
    package_ndc = filters.CharFilter(
        field_name='products__packages__code',
        lookup_expr='icontains',
        distinct=True)
    product_ndc = filters.CharFilter(
        field_name='products__code',
        lookup_expr='icontains',
        distinct=True)
    product_name = filters.CharFilter(
        field_name='products__name',
        lookup_expr='icontains',
        distinct=True)
    inactive_ingredient_name = filters.CharFilter(
        field_name='products__inactive_ingredients__name',
        lookup_expr='icontains',
        distinct=True)
    inactive_ingredient_unii = filters.CharFilter(
        field_name='products__inactive_ingredients__unii',
        lookup_expr='icontains',
        distinct=True)
    schedule = filters.MultipleChoiceFilter(
        field_name='products__schedule',
        choices=SCHEDULE_CHOICES,
        distinct=True)

    class Meta:
        model = Spl
        fields = []
