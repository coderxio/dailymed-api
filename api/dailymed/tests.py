from django.test import TestCase

from rest_framework.test import APIClient

from dailymed.models import Set, Spl, Product, InactiveIngredient, Package


def sample_data(**params):
    """Creates sample data to load into database"""
    default = {'id': 'a43fa2d7-fea0-264d-e053-2995a90acc65',
               'labeler': 'REMEDYREPACK INC.',
               'products': [{'active_ing': ['DULOXETINE HYDROCHLORIDE'],
                             'code': '70518-0343',
                             'name': 'Duloxetine',
                             'packages': [{'code': '70518-0343-0'},
                            {'code': '70518-0343-1'}]}],
               'set_id': '78a5056b-23dc-4897-8909-77eacdedd27b'}

    return default


class PublicApiTest(TestCase):
    """Test public daily med API"""

    def setUp(self):
        self.client = APIClient()

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
            spl=spl
        )

        expected_str = f"{product.code} -- {product.name} -- {product.spl}"
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
            code="0093-0832-01",
            product=product
        )

        expected_str = f"{package.code} -- {package.product}"
        self.assertEqual(str(package), expected_str)