from django.shortcuts import render
from .forms import LatLongForm
from .models import IrradGraph

from nrel_api.solar_api import clean_raw_df, load_raw_df, calc_monthly_averages, display_csv_graph, retrieve_data_from_api, COORD_DECIMAL_PLACES


def irrad_graph_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = LatLongForm(request.POST)
        if form.is_valid():
            monthly_averages = None

            input_lat = form.cleaned_data['lat']
            input_long = form.cleaned_data['long']
            input_year = form.cleaned_data['year']

            obj, created = IrradGraph.objects.get_or_create(lat=input_lat, long=input_long, year=input_year)

            if not obj.csv_file:
                csv_filepath = retrieve_data_from_api(lat=input_lat, long=input_long, year=input_year)
                obj.csv_file = csv_filepath
                obj.save()

            if not obj.metadata:
                raw_df = load_raw_df(obj.csv_file)
                metadata, df = clean_raw_df(raw_df, input_year)
                monthly_averages = calc_monthly_averages(df)
                obj.metadata = metadata
                obj.save()

            if not obj.image:
                if monthly_averages is None:
                    raw_df = load_raw_df(obj.csv_file)
                    metadata, df = clean_raw_df(raw_df, input_year)
                    monthly_averages = calc_monthly_averages(df)

                img_filepath = display_csv_graph(monthly_averages, lat=input_lat, long=input_long, year=input_year)
                obj.image = img_filepath
                obj.save()

            context = {
                'form': form,
                'obj': obj,
            }
            return render(request, 'irrad_graph/irrad_graph_page.html', context)

        # if form is invalid, re-render form with errors
        else:
            return render(request, 'irrad_graph/irrad_graph_page.html', {'form': form, 'obj': None})

    form = LatLongForm()
    context = {
        'form': form,
        'obj': None,
    }

    return render(request, 'irrad_graph/irrad_graph_page.html', context)
