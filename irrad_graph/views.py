from django.shortcuts import render
from .forms import LatLongForm
from .models import IrradGraph

from API.solar_api import clean_raw_df, load_raw_df, calc_monthly_averages, display_csv_graph


def irrad_graph_view(request, *args, **kwargs):
    monthly_averages = None

    csv_file = 'solar_info20200228184632.csv'
    input_lat = 33.21
    input_long = -97.14
    input_year = 2009

    obj, created = IrradGraph.objects.get_or_create(lat=input_lat, long=input_long, year=input_year)

    if not obj.metadata:
        raw_df = load_raw_df(csv_file)
        metadata, df = clean_raw_df(raw_df)
        monthly_averages = calc_monthly_averages(df)
        obj.metadata = metadata
        obj.save()

    if not obj.image:
        if not monthly_averages:
            raw_df = load_raw_df(csv_file)
            metadata, df = clean_raw_df(raw_df)
            monthly_averages = calc_monthly_averages(df)

        img_filepath = display_csv_graph(monthly_averages, lat=input_lat, long=input_long, year=input_year)
        obj.image = img_filepath
        obj.save()

    form = LatLongForm()
    context = {
        'form': form,
        'obj': obj,
    }

    return render(request, 'irrad_graph/irrad_graph_page.html', context)
