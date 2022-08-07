import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from pvlib_api.api_utils import setup_pv_system, clean_all_modules_or_inverters_df
from pvlib import pvsystem
from pvlib.location import Location
from pvlib.modelchain import ModelChain
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS


class BuildPVAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pv_results = setup_pv_system()
        print(pv_results.__dict__)

        return Response({'results': pv_results.__dict__})


class PVSystemInfoAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # TODO: all this stuff with grabbing the whole db and cleaning the data is a bad idea, find a better way to retrieve model/inverter
        # get entire module database
        all_modules_df = pvsystem.retrieve_sam('CECMod')
        all_modules_df = clean_all_modules_or_inverters_df(all_modules_df)

        # get entire inverter database
        all_inverters_df = pvsystem.retrieve_sam('CECInverter')
        all_inverters_df = clean_all_modules_or_inverters_df(all_inverters_df)

        # get the first module and first inverter from their respective dfs
        test_module = all_modules_df.iloc[1]
        test_inverter = all_inverters_df.iloc[1]

        # for now just grab the module and inverter from the example
        sandia_modules = pvsystem.retrieve_sam('SandiaMod')
        cec_inverters = pvsystem.retrieve_sam('cecinverter')
        sandia_module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
        cec_inverter = cec_inverters['ABB__MICRO_0_25_I_OUTD_US_208__208V_']


        # TODO still don't know what this is
        temperature_model_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']

        location = Location(latitude=32.2, longitude=-110.9)

        system = pvsystem.PVSystem(surface_tilt=20, surface_azimuth=200, module_parameters=sandia_module,
                                   inverter_parameters=cec_inverter,
                                   temperature_model_parameters=temperature_model_parameters)

        mc = ModelChain(system, location)

        # TODO will we get this data from the NREL api or separately?
        weather = pd.DataFrame([[1050, 1000, 100, 30, 5]],
                               columns=['ghi', 'dni', 'dhi', 'temp_air', 'wind_speed'],
                               index=[pd.Timestamp('20170401 1200', tz='US/Arizona')])

        # runs the model on the combo of system, location, and weather
        mc.run_model(weather)

        full_results = mc.results
        print(f'full results:\n{full_results}\n\n')

        results_for_frontend = {
            'aoi': mc.results.aoi.values[0],
            'ac': mc.results.ac.values[0],
            'i_sc': mc.results.dc.i_sc.values[0],
            'i_mp': mc.results.dc.i_mp.values[0],
            'v_oc': mc.results.dc.v_oc.values[0],
            'v_mp': mc.results.dc.v_mp.values[0],
            'p_mp': mc.results.dc.p_mp.values[0],
            'i_x': mc.results.dc.i_x.values[0],
            'i_xx': mc.results.dc.i_xx.values[0],
        }

        return Response(results_for_frontend)
