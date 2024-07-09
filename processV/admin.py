# admin.py
from django.contrib import admin
from .models import GeneralData, ProcessDataHeader, ProcessData, UploadedFile

class GeneralDataAdmin(admin.ModelAdmin):
    list_display = ('sap_reactor_no', 'reactor_name', 'reactor_type', 'sap_material_no',
                    'recipe_id', 'recipe_name', 'recipe_version', 'recipe_last_change',
                    'site', 'name_of_site', 'process_order_no', 'batch_no')
    search_fields = ('sap_reactor_no', 'reactor_name', 'recipe_id', 'recipe_name', 'batch_no')
    list_filter = ('reactor_type', 'recipe_name', 'site', 'name_of_site')

class ProcessDataHeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'type', 'medium', 'unit',
                    'type_group', 'format', 'tag_no', 'value_type',
                    'min_value_pcs', 'max_value_pcs')
    search_fields = ('name', 'description', 'type', 'tag_no', 'value_type')
    list_filter = ('type', 'medium', 'unit', 'type_group', 'value_type')

class ProcessDataAdmin(admin.ModelAdmin):
    list_display = ('batch_no', 'timestamp', 'value')
    search_fields = ('batch_no__batch_no', 'timestamp')
    list_filter = ('timestamp', 'batch_no__batch_no')

class UploadedFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'uploaded_at')
    search_fields = ('file',)
    list_filter = ('uploaded_at',)

admin.site.register(GeneralData, GeneralDataAdmin)
admin.site.register(ProcessDataHeader, ProcessDataHeaderAdmin)
admin.site.register(ProcessData, ProcessDataAdmin)
admin.site.register(UploadedFile, UploadedFileAdmin)
