from django.urls import path
from .api import NRELAPIView


urlpatterns = [
    path("nrel/", NRELAPIView.as_view()),
]
