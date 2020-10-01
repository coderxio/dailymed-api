from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from dailymed.models import Set, Spl, InactiveIngredient

from dailymed.serializers import SplSerializer

import json
from pathlib import Path


SPL_URL = reverse('spl-list')
PRODUCT_URL = reverse('product-list')
PACKAGE_URL = reverse('package-list')


class PublicApiTest(TestCase):
    """Test public daily med API"""

    def setUp(self):
        self.client = APIClient()

        """Creates sample data for database"""
        cwd = Path(__file__).parent.absolute()
        with open(f'{cwd}/test.json', 'r') as f:
            default = json.load(f)

        for data in default['results']:
            set_id = data.pop('set_id')
            products_data = data.pop('products')

            set_obj = Set.objects.create(id=set_id)

            spl_obj = set_obj.spls.create(**data)

            for product_data in products_data:
                product_data.pop('name')
                packages_data = product_data.pop('packages')
                if 'inactive_ingredients' in product_data:
                    inactive_ingredients_data = product_data\
                        .pop('inactive_ingredients')

                    inactive_ingredients_list = []
                    for inactive_ingredient_data in inactive_ingredients_data:
                        try:
                            ingredient = InactiveIngredient.objects.get(
                                **inactive_ingredient_data
                            )
                            inactive_ingredients_list.append(ingredient)
                        except Exception:
                            ingredient = InactiveIngredient.objects.create(
                                **inactive_ingredient_data
                            )
                            inactive_ingredients_list.append(ingredient)

                product_obj = spl_obj.products.create(**product_data)
                product_obj.inactive_ingredients\
                    .add(*inactive_ingredients_list)

                for package_data in packages_data:
                    product_obj.packages.create(**package_data)

    def test_retrieve_spls(self):
        """Test retriving a spl"""
        res = self.client.get(
            SPL_URL,
            format='json'
            )

        serializer = SplSerializer(Spl.objects.filter(), many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data['results'])

    def test_retrieve_spls_filter_by_set(self):
        """Test retriving a spl by set filter"""
        set = Set.objects.first()
        res = self.client.get(
            SPL_URL,
            {'set_id': set.id},
            format='json')

        serializer = SplSerializer(
            Spl.objects.filter(set__id=set.id), many=True
            )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data['results'])

    def test_retrieve_spls_filter_by_inactive_ing(self):
        """Test retriving a spl by inactive ingredient filter"""
        inactive_ing = 'alcohol'
        res = self.client.get(
            SPL_URL,
            {'inactive_ingredient_name': inactive_ing},
            format='json')

        serializer = SplSerializer(
            Spl.objects.filter(
                products__inactive_ingredients__name__icontains=inactive_ing)
            .distinct(),
            many=True
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data['results'])

    def test_retrieve_spls_filter_by_schedule(self):
        """Test retriving a spl by schedule filter"""
        schedule = 'CIV'
        res = self.client.get(
            SPL_URL,
            {'schedule': schedule},
            format='json')

        serializer = SplSerializer(Spl.objects.filter(
            products__schedule=schedule).distinct(),
            many=True
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data['results'])

    def test_retrieve_spls_filter_by_drug_name(self):
        """Test retriving a spl by drug name filter"""
        name = 'Ciprofloxacin'
        res = self.client.get(
            SPL_URL,
            {'product_name': name},
            format='json')

        serializer = SplSerializer(Spl.objects.filter(
            products__name=name).distinct(),
            many=True
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, res.data['results'])
