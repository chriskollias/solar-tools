from django.shortcuts import render
from .forms import LatLongForm
from .models import IrradGraph

from API.solar_api import clean_raw_df, load_raw_df, calc_monthly_averages, display_csv_graph


def main_view(request, *args, **kwargs):
    raw_df = load_raw_df('solar_info20200228184632.csv')
    metadata, df = clean_raw_df(raw_df)
    monthly_averages = calc_monthly_averages(df)
    img_filepath = display_csv_graph(monthly_averages)
    form = LatLongForm()
    obj = IrradGraph.objects.get_or_create(lat=33.21, long=-97.14, year=2009, image=img_filepath)
    context = {
        'form': form,
        'obj': obj,
        'metadata': metadata,
    }

    return render(request, 'irrad_graph/irrad_graph_page.html', context)
