from django.db import models


# Create your models here.
class IrradGraphInputs(models.Model):
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    year = models.IntegerField()
    image = models.ImageField(default='irrad_graph/empty.png', upload_to='irrad_graph')
