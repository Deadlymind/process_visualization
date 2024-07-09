from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import GeneralData, ProcessDataHeader, ProcessData, UploadedFile
from django.db.models import Q
import pandas as pd
from django.views import View
from .forms import UploadFileForm
import traceback

# GeneralData Views
class GeneralDataListView(ListView):
    model = GeneralData
    template_name = 'general_data_list.html'
    context_object_name = 'general_data_list'
    paginate_by = 10  # Optional: for pagination

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return GeneralData.objects.filter(batch_no__icontains=query)
        return GeneralData.objects.all()

class GeneralDataDetailView(DetailView):
    model = GeneralData
    template_name = 'processV/generaldata_detail.html'
    context_object_name = 'general_data'

class GeneralDataCreateView(CreateView):
    model = GeneralData
    template_name = 'processV/generaldata_form.html'
    fields = '__all__'
    success_url = reverse_lazy('generaldata_list')

class GeneralDataUpdateView(UpdateView):
    model = GeneralData
    template_name = 'processV/generaldata_form.html'
    fields = '__all__'
    success_url = reverse_lazy('generaldata_list')

class GeneralDataDeleteView(DeleteView):
    model = GeneralData
    template_name = 'processV/generaldata_confirm_delete.html'  # Ensure this matches the template path
    success_url = reverse_lazy('generaldata_list')

# ProcessDataHeader Views
class ProcessDataHeaderListView(ListView):
    model = ProcessDataHeader
    template_name = 'processV/processdataheader_list.html'
    context_object_name = 'process_data_header_list'

class ProcessDataHeaderDetailView(DetailView):
    model = ProcessDataHeader
    template_name = 'processV/processdataheader_detail.html'
    context_object_name = 'process_data_header'

class ProcessDataHeaderCreateView(CreateView):
    model = ProcessDataHeader
    template_name = 'processV/processdataheader_form.html'
    fields = '__all__'
    success_url = reverse_lazy('processdataheader_list')

class ProcessDataHeaderUpdateView(UpdateView):
    model = ProcessDataHeader
    template_name = 'processV/processdataheader_form.html'
    fields = '__all__'
    success_url = reverse_lazy('processdataheader_list')

class ProcessDataHeaderDeleteView(DeleteView):
    model = ProcessDataHeader
    template_name = 'processV/processdataheader_confirm_delete.html'
    success_url = reverse_lazy('processdataheader_list')

# ProcessData Views
class ProcessDataListView(ListView):
    model = ProcessData
    template_name = 'processV/processdata_list.html'
    context_object_name = 'process_data_list'

class ProcessDataDetailView(DetailView):
    model = ProcessData
    template_name = 'processV/processdata_detail.html'
    context_object_name = 'process_data'

class ProcessDataCreateView(CreateView):
    model = ProcessData
    template_name = 'processV/processdata_form.html'
    fields = '__all__'
    success_url = reverse_lazy('processdata_list')

class ProcessDataUpdateView(UpdateView):
    model = ProcessData
    template_name = 'processV/processdata_form.html'
    fields = '__all__'
    success_url = reverse_lazy('processdata_list')

class ProcessDataDeleteView(DeleteView):
    model = ProcessData
    template_name = 'processV/processdata_confirm_delete.html'
    success_url = reverse_lazy('processdata_list')

# UploadedFile Views
class UploadedFileListView(ListView):
    model = UploadedFile
    template_name = 'processV/uploadedfile_list.html'
    context_object_name = 'uploaded_file_list'

class UploadedFileDetailView(DetailView):
    model = UploadedFile
    template_name = 'processV/uploadedfile_detail.html'
    context_object_name = 'uploaded_file'

class UploadedFileCreateView(CreateView):
    model = UploadedFile
    template_name = 'processV/uploadedfile_form.html'
    fields = '__all__'
    success_url = reverse_lazy('uploadedfile_list')

class UploadedFileUpdateView(UpdateView):
    model = UploadedFile
    template_name = 'processV/uploadedfile_form.html'
    fields = '__all__'
    success_url = reverse_lazy('uploadedfile_list')

class UploadedFileDeleteView(DeleteView):
    model = UploadedFile
    template_name = 'processV/uploadedfile_confirm_delete.html'
    success_url = reverse_lazy('uploadedfile_list')

# File Upload View


from django.shortcuts import render, redirect
from django.views import View
from .forms import UploadFileForm
from .models import GeneralData, ProcessData
import pandas as pd
import traceback

class UploadFileView(View):
    form_class = UploadFileForm
    template_name = 'processV/upload_file.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        action = request.POST.get('action')
        form = self.form_class(request.POST, request.FILES)

        # Validate form based on the action
        if action == 'upload_generaldata':
            form.fields['batch_no'].required = False
        elif action == 'update_processdata':
            form.fields['batch_no'].required = True

        if form.is_valid():
            file = request.FILES['file']

            if action == 'upload_generaldata':
                return self.handle_generaldata_upload(request, file, form)
            elif action == 'update_processdata':
                batch_no = form.cleaned_data['batch_no']
                return self.handle_processdata_update(request, file, form, batch_no)
        
        return render(request, self.template_name, {'form': form})

    def handle_generaldata_upload(self, request, file, form):
        try:
            print("Starting general data upload")
            data = pd.read_excel(file)
            print(f"Data read from Excel file: {data.head()}")
            
            data.columns = [str(col).strip() for col in data.columns]
            print(f"Normalized columns: {data.columns.tolist()}")

            expected_columns = {
                'SAP Reactor No': 'sap_reactor_no',
                'Reactor Name': 'reactor_name',
                'Reactor Type': 'reactor_type',
                'SAP Material No': 'sap_material_no',
                'Recipe ID': 'recipe_id',
                'Recipe Name': 'recipe_name',
                'Recipe Version': 'recipe_version',
                'Recipe last change': 'recipe_last_change',
                'Timestamp Recipe Start': 'timestamp_recipe_start',
                'Timestamp Start filling': 'timestamp_start_filling',
                'Timestamp End filling': 'timestamp_end_filling',
                'Timestamp Start reaction': 'timestamp_start_reaction',
                'Timestamp End reaction': 'timestamp_end_reaction',
                'Timestamp Start heating': 'timestamp_start_heating',
                'Timestamp End heating': 'timestamp_end_heating',
                'Timestamp Start cooling': 'timestamp_start_cooling',
                'Timestamp End cooling': 'timestamp_end_cooling',
                'Timestamp Start Additivation': 'timestamp_start_additivation',
                'Timestamp End Additivation': 'timestamp_end_additivation',
                'Timestamp Start Sampling': 'timestamp_start_sampling',
                'Timestamp End Sampling': 'timestamp_end_sampling',
                'Timestamp Start Adjusting': 'timestamp_start_adjusting',
                'Timestamp End Adjusting': 'timestamp_end_adjusting',
                'Timestamp Start Filling': 'timestamp_start_filling_2',
                'Timestamp End Filling': 'timestamp_end_filling_2',
                'Timestamp Recipe End': 'timestamp_recipe_end',
                'Product 5 before Batch': 'product_5_before_batch',
                'Product 4 before Batch': 'product_4_before_batch',
                'Product 3 before Batch': 'product_3_before_batch',
                'Product 2 before Batch': 'product_2_before_batch',
                'Product before Batch': 'product_before_batch',
                'Product after Batch': 'product_after_batch',
                'Site': 'site',
                'Name of Site': 'name_of_site',
                'Process Order No': 'process_order_no',
                'Batch No': 'batch_no',
                'Contrl. Config 1 (T_HotOil)': 'control_config_1',
                'Contrl. Config 2 (T_HotOilMixer)': 'control_config_2',
                'Contrl. Config 3 (m_oil_dosing)': 'control_config_3'
            }

            normalized_data = data.rename(columns=expected_columns)
            print(f"Renamed columns: {normalized_data.columns.tolist()}")

            missing_columns = [col for col in expected_columns.values() if col not in normalized_data.columns]
            if missing_columns:
                print(f"Missing columns: {missing_columns}")
                return render(request, self.template_name, {'form': form, 'error': f'Missing columns in the uploaded file: {missing_columns}'})

            for index, row in normalized_data.iterrows():
                print(f"Processing row {index}: {row.to_dict()}")
                GeneralData.objects.update_or_create(
                    sap_reactor_no=row['sap_reactor_no'],
                    defaults=row.drop('sap_reactor_no').to_dict()
                )
            print("General data upload completed successfully")
        except Exception as e:
            error_message = traceback.format_exc()
            print(f"Error processing file: {error_message}")
            return render(request, self.template_name, {'form': form, 'error': f'There was an error processing the file: {str(e)}'})

        return redirect('generaldata_list')

    def handle_processdata_update(self, request, file, form, batch_no):
        try:
            data = pd.read_excel(file)
            data.columns = [
                'date_time', 'recipe_step', 'p_reactor_target', 'p_reactor', 't_hotoil_in_target', 
                't_hotoil_in', 't_hotoil_out', 't_reactor_target', 't_reactor', 'n_stirrer_target', 
                'n_stirrer', 'n_homog_target', 'n_homog', 'i_homog', 'i_stirrer', 'v_exh', 'pos_mh'
            ]

            print(f"Number of rows in the uploaded file: {len(data)}")

            expected_columns = [
                'date_time', 'recipe_step', 'p_reactor_target', 'p_reactor', 't_hotoil_in_target', 
                't_hotoil_in', 't_hotoil_out', 't_reactor_target', 't_reactor', 'n_stirrer_target', 
                'n_stirrer', 'n_homog_target', 'n_homog', 'i_homog', 'i_stirrer', 'v_exh', 'pos_mh'
            ]

            missing_columns = [col for col in expected_columns if col not in data.columns]
            if missing_columns:
                return render(request, self.template_name, {'form': form, 'error': f'Missing columns in the uploaded file: {missing_columns}'})

            try:
                general_data = GeneralData.objects.get(batch_no=batch_no)
            except GeneralData.DoesNotExist:
                return render(request, self.template_name, {'form': form, 'error': 'GeneralData entry not found for batch number.'})

            entries_created = 0

            for index, row in data.iterrows():
                try:
                    ProcessData.objects.create(
                        batch_no=general_data,
                        timestamp=row['date_time'],
                        date_time=row['date_time'],
                        recipe_step=row['recipe_step'],
                        p_reactor_target=row['p_reactor_target'],
                        p_reactor=row['p_reactor'],
                        t_hotoil_in_target=row['t_hotoil_in_target'],
                        t_hotoil_in=row['t_hotoil_in'],
                        t_hotoil_out=row['t_hotoil_out'],
                        t_reactor_target=row['t_reactor_target'],
                        t_reactor=row['t_reactor'],
                        n_stirrer_target=row['n_stirrer_target'],
                        n_stirrer=row['n_stirrer'],
                        n_homog_target=row['n_homog_target'],
                        n_homog=row['n_homog'],
                        i_homog=row['i_homog'],
                        i_stirrer=row['i_stirrer'],
                        v_exh=row['v_exh'],
                        pos_mh=row['pos_mh']
                    )
                    entries_created += 1

                except Exception as e:
                    error_message = traceback.format_exc()
                    print(f"Error processing row {index}: {error_message}")
                    return render(request, self.template_name, {'form': form, 'error': f'There was an error processing the file: {str(e)}'})

            print(f"Number of entries created: {entries_created}")

        except Exception as e:
            error_message = traceback.format_exc()
            print(f"Error processing file: {error_message}")
            return render(request, self.template_name, {'form': form, 'error': f'There was an error processing the file: {str(e)}'})

        return redirect('processdata_list')
