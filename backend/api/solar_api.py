import os
import pandas as pd
import matplotlib.pyplot as plt
from solar_tools.settings import API_KEY, FULL_NAME, REASON_FOR_USE, AFFILIATION, EMAIL, MAILING_LIST, UTC, MEDIA_ROOT

'''
# Declare all variables as strings. Spaces must be replaced with '+', i.e., change 'John Smith' to 'John+Smith'.

# Specify Coordinated Universal Time (UTC), 'true' will use UTC, 'false' will use the local time zone of the data.
# NOTE: In order to use the NSRDB data in SAM, you must specify UTC as 'false'. SAM requires the data to be in the
# local time zone.
utc = 'false'

# See metadata for specified properties, e.g., timezone and elevation
#timezone, elevation = df['Local Time Zone'], df['Elevation']

'''


# the number of decimal places that the API can handle with respect to lat/long coords
COORD_DECIMAL_PLACES = 2


def calc_monthly_averages(df):
    # Calculate monthly averages and put them in new dataframe
    monthly_averages = df.groupby(['Month']).mean()
    return monthly_averages


def retrieve_data_from_api(lat, long, year, interval=30, leap_year='false', attributes='ghi,dhi,dni,wind_speed,air_temperature,solar_zenith_angle'):
    # Declare url string
    url = f'http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({long}%20{lat})&names={year}&leap_day={leap_year}&interval={interval}&utc={UTC}&full_name={FULL_NAME}&email={EMAIL}&affiliation={AFFILIATION}&mailing_list={MAILING_LIST}&reason={REASON_FOR_USE}&api_key={API_KEY}&attributes={attributes}'
    df = pd.read_csv(url, nrows=20000)
    csv_filename = f'solar_info_{lat}_{long}_{year}.csv'
    csv_filepath = os.path.join(MEDIA_ROOT, 'csv', csv_filename)
    df.to_csv(csv_filepath)
    return csv_filepath


def display_csv_graph(monthly_averages, lat, long, year):
    plt.figure(figsize=(8, 8))

    plt.xlabel('Month', fontsize=8)
    plt.xticks(range(1, 13), fontsize=8)
    plt.ylabel('Irradiance W/m^2', fontsize=8)

    line1, = plt.plot(monthly_averages.GHI, label='GHI')
    line2, = plt.plot(monthly_averages.DHI, label='DHI')
    line3, = plt.plot(monthly_averages.DNI, label='DNI')

    line1.set_label('GHI')
    line2.set_label('DHI')
    line3.set_label('DNI')

    plt.legend(prop={'size': 6})
    plt.title(f'Average Monthly Solar Irradiance ({year})')
    plt.tight_layout()
    filename = f'{lat}_{long}_{year}_graph.png'
    relative_img_filepath = f'graph_imgs/{filename}'
    abs_img_filepath = os.path.join(MEDIA_ROOT, relative_img_filepath)
    plt.savefig(abs_img_filepath)
    return relative_img_filepath


def load_raw_df(filepath):
    raw_df = pd.read_csv(filepath)
    return raw_df


def clean_metadata(raw_metadata):
    """
    clean up the metadata by only extracting the fields we want
    """
    metadata = {'source': raw_metadata['Source'], 'location_id': raw_metadata['Location ID'],
                'lat': raw_metadata['Latitude'], 'lon': raw_metadata['Longitude'],
                'time_zone': raw_metadata['Time Zone'], 'elevation': raw_metadata['Elevation']}

    return metadata
