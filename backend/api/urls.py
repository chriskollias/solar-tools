from django.urls import path
from .nrel_api import NRELAPIView


urlpatterns = [
    path("nrel/", NRELAPIView.as_view()),
]
