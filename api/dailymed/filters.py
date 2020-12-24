from django_filters import rest_framework as filters
from dailymed.models import Spl, Set


SCHEDULE_CHOICES = (
    ('', ''),
    ('CII', 'CII'),
    ('CIII', 'CIII'),
    ('CIV', 'CIV'),
    ('CV', 'CV')
)

TTY_CHOICES = (
    ('', ''),
    ('IN', 'IN'),
    ('PIN', 'PIN'),
    ('MIN', 'MIN'),
    ('SCDC', 'SCDC'),
    ('SCDF', 'SCDF'),
    ('SCDG', 'SCDG'),
    ('SCD', 'SCD'),
    ('GPCK', 'GPCK'),
    ('BN', 'BIN'),
    ('SBDC', 'SBDC'),
    ('SBDF', 'SDBF'),
    ('SBDG', 'SBDG'),
    ('SBD', 'SBD'),
    ('BPCK', 'BPCK'),
    ('PSN', 'PSN'),
    ('SY', 'SY'),
    ('TMSY', 'TMSY'),
    ('DF', 'DF'),
    ('ET', 'ET'),
    ('DFG', 'DFG')
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


class SuperFilter(filters.FilterSet):
    set_id = filters.CharFilter(
        field_name='id',
        lookup_expr='iexact',
        distinct=True)
    labeler = filters.CharFilter(
        field_name='spls__labeler',
        lookup_expr='icontains',
        distinct=True)
    package_ndc = filters.CharFilter(
        field_name='spls__products__packages__code',
        lookup_expr='icontains',
        distinct=True)
    product_ndc = filters.CharFilter(
        field_name='spls__products__code',
        lookup_expr='icontains',
        distinct=True)
    product_name = filters.CharFilter(
        field_name='spls__products__name',
        lookup_expr='icontains',
        distinct=True)
    inactive_ingredient_name = filters.CharFilter(
        field_name='spls__products__inactive_ingredients__name',
        lookup_expr='icontains',
        distinct=True)
    inactive_ingredient_unii = filters.CharFilter(
        field_name='spls__products__inactive_ingredients__unii',
        lookup_expr='icontains',
        distinct=True)
    schedule = filters.MultipleChoiceFilter(
        field_name='spls__products__schedule',
        choices=SCHEDULE_CHOICES,
        distinct=True)
    rxcui = filters.CharFilter(
        field_name='rxnorms__rxcui',
        lookup_expr='iexact',
        distinct=True)
    rxstring = filters.CharFilter(
        field_name='rxnorms__rxstring',
        lookup_expr='icontains',
        distinct=True)
    rxtty = filters.MultipleChoiceFilter(
        field_name='rxnorms__rxtty',
        choices=TTY_CHOICES,
        distinct=True)

    class Meta:
        model = Set
        fields = []
