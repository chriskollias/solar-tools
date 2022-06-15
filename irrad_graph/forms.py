from django import forms
from .models import IrradGraphInputs

class LatLongForm(forms.Form):
    latitude = forms.DecimalField(label="Latitude (test with 33.21")
    longitude = forms.DecimalField(label="Longitude (test with -97.14)")
    year = forms.IntegerField(label="Year", min_value=1998, max_value=2014)

    class Meta:
        Model = IrradGraphInputs

        fields = [
            'latitude',
            'longitude',
            'year'
        ]