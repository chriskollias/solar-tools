from django import forms
from API.solar_api import COORD_DECIMAL_PLACES
from irrad_graph.models import IrradGraph


class LatLongForm(forms.Form):
    lat = forms.DecimalField(label="Latitude", decimal_places=COORD_DECIMAL_PLACES)
    long = forms.DecimalField(label="Longitude", decimal_places=COORD_DECIMAL_PLACES)
    year = forms.IntegerField(label="Year", min_value=1998, max_value=2014)

    class Meta:
        Model = IrradGraph

        fields = [
            'lat',
            'long',
            'year'
        ]
