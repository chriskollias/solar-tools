from django.db import models


class IrradGraphInputs(models.Model):
    lat = models.DecimalField(max_digits=7, decimal_places=4)
    long = models.DecimalField(max_digits=7, decimal_places=4)
    year = models.IntegerField()
    image = models.ImageField(default='irrad_graph/empty.png', upload_to='irrad_graph')
