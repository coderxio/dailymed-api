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
        related_name="spls"
    )

class Ndc(models.Model):
    ndc = models.CharField(max_length=15)
    spl = models.ForeignKey(
        Spl,
        on_delete=models.PROTECT,
        related_name="ndcs"
    )
