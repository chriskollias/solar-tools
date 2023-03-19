import pandas as pd
from urllib.parse import urlencode


def format_request_url(base_url, response_format, endpoint, **kwargs):
    request_url = f'{base_url}{endpoint}.{response_format}/?'
    query_params = urlencode(kwargs)
    return request_url + query_params


def clean_raw_df(raw_df):
    """
    clean up the raw dataframe as it is given from the NREL API
    """
    # the first row contains metadata about the requested info
    metadata_row = raw_df.iloc[0, :]
    metadata = metadata_row.to_dict()

    # the second row contains the actual column names
    columns = raw_df.iloc[1, :].values

    # remove any nan/null values from columns
    columns = columns[~pd.isnull(columns)]

    num_columns = len(columns)

    # extract the main body of the data from the raw_df
    data_body = raw_df.iloc[2:, :num_columns]

    # set the data_body's columns to match the extracted column_names
    data_body.columns = columns

    # create a new df that contains the data body now with the correct column names and correct dtypes
    df = pd.DataFrame(data_body, columns=columns)

    """
    .astype(
        {'Year': 'int64', 'Month': 'int64', 'Day': 'int64', 'Hour': 'int64', 'Minute': 'int64', 'GHI': 'float64',
         'DHI': 'float64', 'DNI': 'float64', 'Wind Speed': 'float64', 'Temperature': 'float64',
         'Solar Zenith Angle': 'float64'})
    """

    # reset the cleaned df's index inplace, using the existing index col
    df.reset_index(inplace=True, drop=True)

    return df, metadata


def calc_monthly_averages(df):
    # Calculate monthly averages and put them in new dataframe
    monthly_averages_df = df.groupby(['Month']).mean()
    return monthly_averages_df
