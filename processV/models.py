from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# Constants for max length values
MAX_LENGTH = 100
MAX_LENGTH_DESC = 255
MAX_LENGTH_SHORT = 50

class GeneralData(models.Model):
    sap_reactor_no = models.CharField(max_length=MAX_LENGTH, verbose_name=_("SAP Reactor Number"))
    reactor_name = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Reactor Name"))
    reactor_type = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Reactor Type"))
    sap_material_no = models.CharField(max_length=MAX_LENGTH, verbose_name=_("SAP Material Number"))
    recipe_id = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Recipe ID"))
    recipe_name = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Recipe Name"))
    recipe_version = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Recipe Version"))
    recipe_last_change = models.DateTimeField(verbose_name=_("Last Change of Recipe"))

    # timestamps
    timestamp_recipe_start = models.DateTimeField(verbose_name=_("Recipe Start Time"))
    timestamp_start_filling = models.DateTimeField(verbose_name=_("Start Filling Time"))
    timestamp_end_filling = models.DateTimeField(verbose_name=_("End Filling Time"))
    timestamp_start_reaction = models.DateTimeField(verbose_name=_("Start Reaction Time"))
    timestamp_end_reaction = models.DateTimeField(verbose_name=_("End Reaction Time"))
    timestamp_start_heating = models.DateTimeField(verbose_name=_("Start Heating Time"))
    timestamp_end_heating = models.DateTimeField(verbose_name=_("End Heating Time"))
    timestamp_start_cooling = models.DateTimeField(verbose_name=_("Start Cooling Time"))
    timestamp_end_cooling = models.DateTimeField(verbose_name=_("End Cooling Time"))
    timestamp_start_additivation = models.DateTimeField(verbose_name=_("Start Additivation Time"))
    timestamp_end_additivation = models.DateTimeField(verbose_name=_("End Additivation Time"))
    timestamp_start_sampling = models.DateTimeField(verbose_name=_("Start Sampling Time"))
    timestamp_end_sampling = models.DateTimeField(verbose_name=_("End Sampling Time"))
    timestamp_start_adjusting = models.DateTimeField(verbose_name=_("Start Adjusting Time"))
    timestamp_end_adjusting = models.DateTimeField(verbose_name=_("End Adjusting Time"))
    timestamp_start_filling_2 = models.DateTimeField(verbose_name=_("Start Second Filling Time"))
    timestamp_end_filling_2 = models.DateTimeField(verbose_name=_("End Second Filling Time"))
    timestamp_recipe_end = models.DateTimeField(verbose_name=_("Recipe End Time"))

    # products
    product_5_before_batch = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Product 5 Before Batch"))
    product_4_before_batch = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Product 4 Before Batch"))
    product_3_before_batch = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Product 3 Before Batch"))
    product_2_before_batch = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Product 2 Before Batch"))
    product_before_batch = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Product Before Batch"))
    product_after_batch = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Product After Batch"))

    # site and batch
    site = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Site Name"))
    name_of_site = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Name of Site"))
    process_order_no = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Process Order Number"))
    batch_no = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Batch Number"))

    # control configurations
    control_config_1 = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Control Configuration 1"))
    control_config_2 = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Control Configuration 2"))
    control_config_3 = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Control Configuration 3"))

    def __str__(self):
        return f"Batch No: {self.batch_no}, Recipe Name: {self.recipe_name}"

class ProcessDataHeader(models.Model):
    row = models.IntegerField(default=0, verbose_name=_("Row Number"))
    name = models.CharField(max_length=MAX_LENGTH, verbose_name=_("Header Name"))
    description = models.CharField(max_length=MAX_LENGTH_DESC, blank=True, null=True, verbose_name=_("Description"))
    type = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True, null=True, verbose_name=_("Type"))
    medium = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True, null=True, verbose_name=_("Medium"))
    unit = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True, null=True, verbose_name=_("Unit"))
    type_group = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True, null=True, verbose_name=_("Type Group"))
    format = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True, null=True, verbose_name=_("Format"))
    tag_no = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True, null=True, verbose_name=_("Tag Number"))
    value_type = models.CharField(max_length=MAX_LENGTH_SHORT, blank=True, null=True, verbose_name=_("Value Type"))
    min_value_pcs = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0)], verbose_name=_("Minimum Value PCS"))
    max_value_pcs = models.FloatField(blank=True, null=True, validators=[MaxValueValidator(10000)], verbose_name=_("Maximum Value PCS"))

    def __str__(self):
        return f"Header: {self.name}, Row: {self.row}"



class ProcessData(models.Model):
    batch_no = models.ForeignKey(GeneralData, on_delete=models.CASCADE, related_name='process_data', verbose_name=_("Batch Number"))
    timestamp = models.DateTimeField(verbose_name=_("Timestamp"))
    value = models.FloatField(default=0.0, verbose_name=_("Value"))

    # Newly added fields with default values
    date_time = models.DateTimeField(default=timezone.now, verbose_name=_("Date Time"))
    recipe_step = models.IntegerField(default=0, verbose_name=_("Recipe Step"))
    p_reactor_target = models.FloatField(default=0.0, verbose_name=_("Reactor Pressure Target"))
    p_reactor = models.FloatField(default=0.0, verbose_name=_("Reactor Pressure"))
    t_hotoil_in_target = models.FloatField(default=0.0, verbose_name=_("Hot Oil Inlet Temperature Target"))
    t_hotoil_in = models.FloatField(default=0.0, verbose_name=_("Hot Oil Inlet Temperature"))
    t_hotoil_out = models.FloatField(default=0.0, verbose_name=_("Hot Oil Outlet Temperature"))
    t_reactor_target = models.FloatField(default=0.0, verbose_name=_("Reactor Temperature Target"))
    t_reactor = models.FloatField(default=0.0, verbose_name=_("Reactor Temperature"))
    n_stirrer_target = models.FloatField(default=0.0, verbose_name=_("Stirrer Speed Target"))
    n_stirrer = models.FloatField(default=0.0, verbose_name=_("Stirrer Speed"))
    n_homog_target = models.FloatField(default=0.0, verbose_name=_("Homogenizer Speed Target"))
    n_homog = models.FloatField(default=0.0, verbose_name=_("Homogenizer Speed"))
    i_homog = models.FloatField(default=0.0, verbose_name=_("Homogenizer Current"))
    i_stirrer = models.FloatField(default=0.0, verbose_name=_("Stirrer Current"))
    v_exh = models.FloatField(default=0.0, verbose_name=_("Exhaust Valve"))
    pos_mh = models.IntegerField(default=0, verbose_name=_("Manhole Position"))

    def __str__(self):
        return f"Batch: {self.batch_no.batch_no}, Timestamp: {self.timestamp}"

    class Meta:
        verbose_name = _("Process Data")
        verbose_name_plural = _("Process Data")
        ordering = ['timestamp']


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/', verbose_name=_("File"))
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Uploaded At"))

    def __str__(self):
        return f"File uploaded at {self.uploaded_at}"
