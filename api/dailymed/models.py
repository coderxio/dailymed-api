from django.db import models


class Set(models.Model):
    """Dailymed set model which can contain multiple spl files"""
    name = models.CharField(100)


class Spl(models.Model):
    """Dailymed model for individual spl xml files"""
    name = models.CharField(100)
    set = models.ForeignKey(
        Set,
        on_delete=models.PROTECT,
        related_name="spls"
    )

class Ndc(models.Model):
    value = models.CharField(15)
    spl = models.ForeignKey(
        Spl,
        on_delete=models.PROTECT,
        related_name="ndcs"
    )
