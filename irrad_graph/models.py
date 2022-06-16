import os
from django.db import models
from solar_tools.settings import MEDIA_ROOT


class IrradGraph(models.Model):
    lat = models.DecimalField(max_digits=5, decimal_places=2)
    long = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()
    image = models.ImageField(upload_to='media/graph_imgs', null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    csv_file = models.FileField(upload_to='media/csv', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'IrradGraphs'
