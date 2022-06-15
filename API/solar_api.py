import os
import pandas as pd
import matplotlib.pyplot as plt
import time
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


def calc_monthly_averages(df):
    # Calculate monthly averages and put them in new dataframe
    monthly_averages = df.groupby(['Month']).mean()
    return monthly_averages


def retrieve_data_from_api(lat, lon, year, interval, leap_year, attributes):
    # Declare url string
    url = f'http://developer.nrel.gov/api/solar/nsrdb_psm3_download.csv?wkt=POINT({lon}%20{lat})&names={year}&leap_day={leap_year}&interval={interval}&utc={UTC}&full_name={FULL_NAME}&email={EMAIL}&affiliation={AFFILIATION}&mailing_list={MAILING_LIST}&reason={REASON_FOR_USE}&api_key={API_KEY}&attributes={attributes}'
    print(url)
    df = pd.read_csv(url, nrows=20000)
    timestr = time.strftime("%Y%m%d%H%M%S")
    filename = 'solar_info' + timestr + '.csv'
    df.to_csv(filename)
    return filename


def display_csv_graph(monthly_averages):
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
    plt.title('Average Monthly Solar Irradiance')
    plt.tight_layout()
    filename = 'graph.png'
    relative_img_filepath = f'graph_imgs/{filename}'
    abs_img_filepath = os.path.join(MEDIA_ROOT, relative_img_filepath)
    plt.savefig(abs_img_filepath)
    return relative_img_filepath


def load_raw_df(filepath):
    raw_df = pd.read_csv(filepath)
    return raw_df


def clean_raw_df(raw_df):
    """
    clean up the raw dataframe as it is given from the NREL API
    """
    # the first row contains metadata about the requested info
    metadata_row = raw_df.iloc[0, :]

    # the second row contains the actual column names
    column_names = raw_df.iloc[1, 1:12].values

    # extract the main body of the data from the raw_df
    data_body = raw_df.iloc[2:, 1:12]

    # set the data_body's columns to match the extracted column_names
    data_body.columns = column_names

    # create a new df that contains the data body now with the correct column names and correct dtypes
    df = pd.DataFrame(data_body, columns=column_names).astype(
        {'Year': 'int64', 'Month': 'int64', 'Day': 'int64', 'Hour': 'int64', 'Minute': 'int64', 'GHI': 'float64',
         'DHI': 'float64', 'DNI': 'float64', 'Wind Speed': 'float64', 'Temperature': 'float64',
         'Solar Zenith Angle': 'float64'})

    # clean up the metadata
    metadata = clean_metadata(metadata_row.to_dict())

    return metadata, df


def clean_metadata(raw_metadata):
    """
    clean up the metadata by only extracting the fields we want
    """
    metadata = {'source': raw_metadata['Source'], 'location_id': raw_metadata['Location ID'],
                'lat': raw_metadata['Latitude'], 'lon': raw_metadata['Longitude'],
                'time_zone': raw_metadata['Time Zone'], 'elevation': raw_metadata['Elevation']}

    return metadata
