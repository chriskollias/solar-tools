from django.shortcuts import render
from .forms import LatLongForm
from .models import IrradGraphInputs
import matplotlib.pyplot as plt

from API.solar_api import NREL_API


# Create your views here.
def main_view(request, *args, **kwargs):
    APP_MEDIA_PATH = 'irrad_graph/'
    APP_SAVE_LOCATION = 'media/irrad_graph/'

    form = LatLongForm()
    obj = None

    if request.method == 'POST':
        form = LatLongForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            year = form.cleaned_data['year']
            #attrs = 'ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'
            attrs = 'ghi,dhi,dni'
            print(f'lat:{latitude} long:{longitude} year:{year} attrs:{attrs}')

            api = NREL_API()
            graph_image = api.get_monthly_averages(latitude, longitude, year, attrs)
            image_path = APP_MEDIA_PATH + graph_image
            APP_SAVE_LOCATION += graph_image
            plt.savefig(APP_SAVE_LOCATION, dpi=300)
            form.cleaned_data['image'] = image_path
            obj = IrradGraphInputs.objects.create(**form.cleaned_data)

            form = LatLongForm()
        else:
            print(form.errors)

    context = {
        'form': form,
        'obj': obj,
    }
    return render(request, 'irrad_graph/irrad_graph_page.html', context)