from django.test import TestCase

from dailymed.models import Set, Spl, Product, InactiveIngredient, Package

import json
from pathlib import Path


class DatabaseTest(TestCase):
    """Test database creation and structure"""

    def setUp(self):
        """Creates sample data to load into database"""
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

    def test_create_set(self):
        """Test creation of set in db"""
        obj1 = Set.objects.first()
        obj2 = Set.objects.last()

        self.assertEqual(str(obj1), obj1.id)
        self.assertEqual(str(obj2), obj2.id)

    def test_create_spl(self):
        """Test creation of spl in db"""
        obj1 = Spl.objects.first()
        obj2 = Spl.objects.last()

        expected_str1 = f"{obj1.id} -- {obj1.set} -- {obj1.labeler}"

        self.assertEqual(str(obj1), expected_str1)
        self.assertNotEqual(str(obj2), expected_str1)

    def test_create_product(self):
        """Test creation of product in db"""
        obj1 = Product.objects.first()
        obj2 = Product.objects.last()

        expected_str1 = f"{obj1.code} -- {obj1.name} -- " \
            f"{obj1.schedule} -- {obj1.spl}"
        self.assertEqual(str(obj1), expected_str1)
        self.assertNotEqual(str(obj2), expected_str1)

    def test_create_inactive_ingredient(self):
        """Test creation of inactive ingredient in db"""
        obj1 = InactiveIngredient.objects.first()
        obj2 = InactiveIngredient.objects.last()

        expected_str1 = f"{obj1.name} -- {obj1.unii}"
        self.assertEqual(str(obj1), expected_str1)
        self.assertNotEqual(str(obj2), expected_str1)

    def test_create_package(self):
        """Test creation of package in db"""
        obj1 = Package.objects.first()
        obj2 = Package.objects.last()

        expected_str1 = f"{obj1.code} -- {obj1.product}"
        self.assertEqual(str(obj1), expected_str1)
        self.assertNotEqual(str(obj2), expected_str1)
