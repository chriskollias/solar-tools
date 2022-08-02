from rest_framework.response import Response
from rest_framework.views import APIView
from pvlib_api.api_utils import setup_pv_system


class BuildPVAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pv_results = setup_pv_system()
        print(pv_results.__dict__)

        return Response({'results': pv_results.__dict__})
