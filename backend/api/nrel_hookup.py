import io
import pandas as pd
import requests
from solar_tools.settings import API_KEY, FULL_NAME, REASON_FOR_USE, AFFILIATION, EMAIL, MAILING_LIST, UTC
from .api_utils import format_request_url, clean_raw_df

BASE_URL = "http://developer.nrel.gov"

# csv or json
RESPONSE_FORMAT = 'csv'

# using the Physical Solar Model (PSM) v3 - Five Minute Temporal Resolution
# https://developer.nrel.gov/docs/solar/nsrdb/psm3-5min-download/
ENDPOINT = f'/api/nsrdb/v2/solar/psm3-5min-download'


def send_data_request(wkt, attributes, years):
    request_url = format_request_url(BASE_URL, RESPONSE_FORMAT, ENDPOINT, api_key=API_KEY, wkt=wkt, attributes=attributes, names=years, utc="true",
                                     leap_day="true", interval=30, full_name=FULL_NAME, email=EMAIL, affiliation=AFFILIATION, reason=REASON_FOR_USE, mailing_list=MAILING_LIST)

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }

    # print('full url:')
    # print(request_url)

    response = requests.request("GET", request_url, headers=headers)

    if response.ok:
        df = pd.read_csv(io.StringIO(response.text))
        df, metadata = clean_raw_df(df)
        return {
            "df": df,
            "metadata": metadata,
            "error": False
        }
    elif response.status_code == 429:
        print("rate limit exceeded")
        print(response)
        return {
            "error": True,
            "status_code": response.status_code,
            "error_description": "rate limit exceeded"
        }
    else:
        print('NREL response problem, printing response.text')
        print(response.text, '\n')

        errors = "Unknown error"
        try:
            errors = ", ".join(response.json()['errors'])
        except:
            print("Could not get errors from response json")
            print(response.text, '\n')

        return {
            "error": True,
            "status_code": response.status_code,
            "error_description": errors
        }


def test_nrel_api():
    wkt = 'POINT(-108.5449 40.5137)'
    years = '2018'
    attributes = 'air_temperature,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,dhi,dni,fill_flag,ghi,relative_humidity,solar_zenith_angle,surface_albedo,surface_pressure,total_precipitable_water,wind_direction,wind_speed'

    response = send_data_request(wkt, attributes, years)
    return response
