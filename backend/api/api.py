import io
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .api_utils import organize_response_data
from .nrel_hookup import send_data_request


class NRELAPIView(APIView):

    def post(self, request, *args, **kwargs):
        request_body = json.loads(request.body)
        lat = request_body.get('lat')
        lon = request_body.get('lon')

        # TODO: handle any rounding of user input here if necessary

        # generate well-known text string of coordinates
        wkt_string = f'POINT({lon} {lat})'

        # TODO just hardcoding these in for now
        years = '2018'
        attributes = 'air_temperature,clearsky_dhi,clearsky_dni,clearsky_ghi,cloud_type,dew_point,dhi,dni,fill_flag,ghi,relative_humidity,solar_zenith_angle,surface_albedo,surface_pressure,total_precipitable_water,wind_direction,wind_speed'

        nrel_response_data = send_data_request(wkt_string, attributes, years)

        # TODO handle different error status codes differently
        if nrel_response_data.get('error'):
            return Response({"detail": nrel_response_data.get('error_description')}, status=status.HTTP_400_BAD_REQUEST)

        # if not an error, turn the dataframe into a dict for the response
        df = nrel_response_data.get('df')

        # df.to_csv('demo.csv')

        nrel_data = organize_response_data(df)
        return Response(nrel_data)
