from django.db import models


class Set(models.Model):
    """DailyMed set model which can contain multiple spl files"""
    id = models.CharField(max_length=100, primary_key=True)

    # Str method used for testing database creation in test.py
    def __str__(self):
        return self.id


class Spl(models.Model):
    """DailyMed model for individual spl xml files"""
    id = models.CharField(max_length=100, primary_key=True)
    set = models.ForeignKey(
        Set,
        on_delete=models.PROTECT,
        related_name='spls',
    )
    labeler = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.id} -- {self.set} -- {self.labeler}"


class Product(models.Model):
    """Product level model"""
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    schedule = models.CharField(max_length=10)
    spl = models.ForeignKey(
        Spl,
        on_delete=models.PROTECT,
        related_name='products',
    )
    inactive_ingredients = models.ManyToManyField(
        'InactiveIngredient',
        related_name='products',
    )

    def __str__(self):
        return f"{self.code} -- {self.name} -- {self.spl}"


class InactiveIngredient(models.Model):
    """Inactive ingredient for each product"""
    name = models.CharField(max_length=255)
    unii = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} -- {self.unii}"


class Package(models.Model):
    """Package level model"""
    code = models.CharField(max_length=20)
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='packages'
    )

    def __str__(self):
        return f"{self.code} -- {self.product}"
