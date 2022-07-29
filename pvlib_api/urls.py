from django.urls import path
from pvlib_api.api import BuildPVAPIView

urlpatterns = [
    path('', BuildPVAPIView.as_view(), name='build-pv-api'),
]
