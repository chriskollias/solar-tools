from django.urls import path
from .views import irrad_graph_view

app_name = 'irrad_graph'

urlpatterns = [
    path('', irrad_graph_view, name='main-view'),
]
