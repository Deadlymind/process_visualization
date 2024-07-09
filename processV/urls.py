from django.urls import path
from .views import (
    GeneralDataListView, GeneralDataDetailView, GeneralDataCreateView,
    GeneralDataUpdateView, GeneralDataDeleteView,
    ProcessDataHeaderListView, ProcessDataHeaderDetailView, ProcessDataHeaderCreateView,
    ProcessDataHeaderUpdateView, ProcessDataHeaderDeleteView,
    ProcessDataListView, ProcessDataDetailView, ProcessDataCreateView,
    ProcessDataUpdateView, ProcessDataDeleteView,
    UploadedFileListView, UploadedFileDetailView, UploadedFileCreateView,
    UploadedFileUpdateView, UploadedFileDeleteView, UploadFileView,
)
from chart.views import chart_view, process_data_chart


urlpatterns = [
    path('', GeneralDataListView.as_view(), name='generaldata_list'),
    path('generaldata/<int:pk>/', GeneralDataDetailView.as_view(), name='generaldata_detail'),
    path('generaldata/create/', GeneralDataCreateView.as_view(), name='generaldata_create'),
    path('generaldata/add/', GeneralDataCreateView.as_view(), name='generaldata_add'),
    path('generaldata/update/<int:pk>/', GeneralDataUpdateView.as_view(), name='generaldata_update'),
    path('generaldata/delete/<int:pk>/', GeneralDataDeleteView.as_view(), name='generaldata_delete'),
    path('generaldata/edit/<int:pk>/', GeneralDataUpdateView.as_view(), name='generaldata_edit'),
    
    path('generaldata/<int:pk>/chart/', chart_view, name='generaldata_chart'), 

    path('processdataheader/', ProcessDataHeaderListView.as_view(), name='processdataheader_list'),
    path('processdataheader/<int:pk>/', ProcessDataHeaderDetailView.as_view(), name='processdataheader_detail'),
    path('processdataheader/create/', ProcessDataHeaderCreateView.as_view(), name='processdataheader_create'),
    path('processdataheader/update/<int:pk>/', ProcessDataHeaderUpdateView.as_view(), name='processdataheader_update'),
    path('processdataheader/delete/<int:pk>/', ProcessDataHeaderDeleteView.as_view(), name='processdataheader_delete'),

    path('processdata/', ProcessDataListView.as_view(), name='processdata_list'),
    path('processdata/<int:pk>/', ProcessDataDetailView.as_view(), name='processdata_detail'),
    path('processdata/create/', ProcessDataCreateView.as_view(), name='processdata_create'),
    path('processdata/update/<int:pk>/', ProcessDataUpdateView.as_view(), name='processdata_update'),
    path('processdata/delete/<int:pk>/', ProcessDataDeleteView.as_view(), name='processdata_delete'),

    path('uploadedfile/', UploadedFileListView.as_view(), name='uploadedfile_list'),
    path('uploadedfile/<int:pk>/', UploadedFileDetailView.as_view(), name='uploadedfile_detail'),
    path('uploadedfile/create/', UploadedFileCreateView.as_view(), name='uploadedfile_create'),
    path('uploadedfile/update/<int:pk>/', UploadedFileUpdateView.as_view(), name='uploadedfile_update'),
    path('uploadedfile/delete/<int:pk>/', UploadedFileDeleteView.as_view(), name='uploadedfile_delete'),

    path('upload/', UploadFileView.as_view(), name='upload_file'),

    path('process_data_chart/', process_data_chart, name='process_data_chart'),  # Ensure this is included
]
