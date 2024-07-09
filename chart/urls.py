from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.chart_view, name='chart_view'),
    path('chart/data/', views.process_data_chart, name='process_data_chart'),
]
