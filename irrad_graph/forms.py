from django import forms
from .models import IrradGraph


class LatLongForm(forms.Form):
    lat = forms.DecimalField(label="Latitude (test with 33.21)")
    long = forms.DecimalField(label="Longitude (test with -97.14)")
    year = forms.IntegerField(label="Year", min_value=1998, max_value=2014)

    class Meta:
        Model = IrradGraph

        fields = [
            'lat',
            'long',
            'year'
        ]