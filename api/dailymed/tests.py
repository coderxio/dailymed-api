from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from dailymed.models import Set, Spl, Product, InactiveIngredient, Package

from dailymed.serializers import SplSerializer, ProductSerializer
from dailymed.serializers import PackageSerializer


def sample_data(**params):
    """Creates sample data to load into database"""
    default = {'id': 'a43fa2d7-fea0-264d-e053-2995a90acc65',
               'labeler': 'REMEDYREPACK INC.',
               'products': [{'active_ing': ['DULOXETINE HYDROCHLORIDE'],
                             'code': '70518-0343',
                             'name': 'Duloxetine',
                             'schedule': 'legend',
                             'packages': [{'code': '70518-0343-0'},
                            {'code': '70518-0343-1'}]}],
               'set_id': '78a5056b-23dc-4897-8909-77eacdedd27b'}

    return default


SPL_URL = reverse('spl-list')
PRODUCT_URL = reverse('product-list')
PACKAGE_URL = reverse('package-list')


class DatabaseTest(TestCase):
    """Test database creation and structure"""

    def test_create_set(self):
        """Test creation of set in db"""
        set_obj = Set.objects.create(id=sample_data()['set_id'])

        self.assertEqual(str(set_obj), set_obj.id)

    def test_create_spl(self):
        """Test creation of spl in db"""
        data = sample_data()

        set_obj = Set.objects.create(id=data['set_id'])

        spl = Spl.objects.create(
            id=data['id'],
            set=set_obj,
            labeler=data['labeler']
        )

        expected_str = f"{spl.id} -- {spl.set} -- {spl.labeler}"
        self.assertEqual(str(spl), expected_str)

    def test_create_product(self):
        data = sample_data()

        set_obj = Set.objects.create(id=data['set_id'])
        spl = Spl.objects.create(
            id=data['id'],
            set=set_obj,
            labeler=data['labeler']
        )

        product = Product.objects.create(
            code=data['products'][0]['code'],
            name=data['products'][0]['name'],
            schedule=data['products'][0]['schedule'],
            spl=spl
        )

        expected_str = f"{product.code} -- {product.name} -- {product.schedule} -- {product.spl}"
        self.assertEqual(str(product), expected_str)

    def test_create_inactive_ingredient(self):
        ingredient = InactiveIngredient.objects.create(
            name="MICROCRYSTALLINE CELLULOSE",
            unii="OP1R32D61U"
        )

        expected_str = f"{ingredient.name} -- {ingredient.unii}"
        self.assertEqual(str(ingredient), expected_str)

    def test_create_package(self):
        data = sample_data()

        set_obj = Set.objects.create(id=data['set_id'])
        spl = Spl.objects.create(
            id=data['id'],
            set=set_obj,
            labeler=data['labeler']
        )

        product = Product.objects.create(
            code=data['products'][0]['code'],
            name=data['products'][0]['name'],
            spl=spl
        )

        package = Package.objects.create(
            code=data['products'][0]['packages'][0]['code'],
            product=product
        )

        expected_str = f"{package.code} -- {package.product}"
        self.assertEqual(str(package), expected_str)


class PublicApiTest(TestCase):
    """Test public daily med API"""

    def setUp(self):
        self.client = APIClient()

        # Construct sample data in temp DB
        data = sample_data()
        set_obj = Set.objects.create(id=data['set_id'])
        spl = Spl.objects.create(
            id=data['id'],
            set=set_obj,
            labeler=data['labeler']
        )
        product = Product.objects.create(
            code=data['products'][0]['code'],
            name=data['products'][0]['name'],
            spl=spl
        )
        package = Package.objects.create(
            code=data['products'][0]['packages'][0]['code'],
            product=product
        )

        self.set = set_obj
        self.spl = spl
        self.product = product
        self.package = package

        self.ingredient = InactiveIngredient.objects.create(
            name="MICROCRYSTALLINE CELLULOSE",
            unii="OP1R32D61U"
        )

    def test_retrieve_spl(self):
        """Test retriving a spl"""
        res = self.client.get(SPL_URL, format='json')

        serializer = SplSerializer(self.spl)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn(serializer.data, res.data)

    def test_retrieve_product(self):
        """Test retriving a product"""
        res = self.client.get(PRODUCT_URL, format='json')

        serializer = ProductSerializer(self.product)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn(serializer.data, res.data)

    def test_retrieve_package(self):
        """Test retriving a package"""
        res = self.client.get(PACKAGE_URL, format='json')

        serializer = PackageSerializer(self.package)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn(serializer.data, res.data)
