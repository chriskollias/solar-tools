import folium
import os
from solar_tools.settings import MEDIA_ROOT

DEFAULT_ZOOM_START = 14


def generate_map(lat, long, zoom_start=DEFAULT_ZOOM_START):
    map = folium.Map(location=(lat, long), zoom_start=zoom_start, tiles='Stamen Terrain')
    map_filename = generate_map_filename(lat, long, zoom_start)
    map_filepath = os.path.join(MEDIA_ROOT, 'map_htmls', map_filename)
    map.save(map_filepath)
    return map_filepath


def generate_map_filename(lat, long, zoom_start=DEFAULT_ZOOM_START):
    return f'{lat}_{long}_{zoom_start}_map.html'


def check_if_map_file_exists(map_filename):
    map_filepath = os.path.join(MEDIA_ROOT, 'map_htmls', map_filename)
    return os.path.isfile(map_filepath)
