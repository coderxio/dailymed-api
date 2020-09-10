from django.db import models


class Set(models.Model):
    """DailyMed set model which can contain multiple spl files"""
    id = models.CharField(max_length=100, primary_key=True)


class Spl(models.Model):
    """DailyMed model for individual spl xml files"""
    id = models.CharField(max_length=100, primary_key=True)
    set = models.ForeignKey(
        Set,
        on_delete=models.PROTECT,
        related_name='spls',
    )
    labeler = models.CharField(max_length=200)


class Product(models.Model):
    """Product level model"""
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    spl = models.ForeignKey(
        Spl,
        on_delete=models.PROTECT,
        related_name='products',
    )


class Package(models.Model):
    """Package level model"""
    code = models.CharField(max_length=20)
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='packages'
    )
