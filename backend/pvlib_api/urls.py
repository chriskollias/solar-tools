from django.urls import path
from pvlib_api.api import BuildPVAPIView, PVSystemInfoAPIView

urlpatterns = [
    path('pvsystem', PVSystemInfoAPIView.as_view()),
    path('', BuildPVAPIView.as_view()),
]
