from django.db import models


class IrradGraph(models.Model):
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    long = models.DecimalField(max_digits=7, decimal_places=4)
    year = models.IntegerField()
    image = models.ImageField(upload_to='irrad_graph', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'IrradGraphs'
