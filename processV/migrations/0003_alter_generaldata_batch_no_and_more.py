# Generated by Django 5.0.6 on 2024-07-07 21:04

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processV', '0002_alter_processdata_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaldata',
            name='batch_no',
            field=models.CharField(max_length=100, verbose_name='Batch Number'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='control_config_1',
            field=models.CharField(max_length=100, verbose_name='Control Configuration 1'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='control_config_2',
            field=models.CharField(max_length=100, verbose_name='Control Configuration 2'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='control_config_3',
            field=models.CharField(max_length=100, verbose_name='Control Configuration 3'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='name_of_site',
            field=models.CharField(max_length=100, verbose_name='Name of Site'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='process_order_no',
            field=models.CharField(max_length=100, verbose_name='Process Order Number'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='product_2_before_batch',
            field=models.CharField(max_length=100, verbose_name='Product 2 Before Batch'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='product_3_before_batch',
            field=models.CharField(max_length=100, verbose_name='Product 3 Before Batch'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='product_4_before_batch',
            field=models.CharField(max_length=100, verbose_name='Product 4 Before Batch'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='product_5_before_batch',
            field=models.CharField(max_length=100, verbose_name='Product 5 Before Batch'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='product_after_batch',
            field=models.CharField(max_length=100, verbose_name='Product After Batch'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='product_before_batch',
            field=models.CharField(max_length=100, verbose_name='Product Before Batch'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='reactor_name',
            field=models.CharField(max_length=100, verbose_name='Reactor Name'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='reactor_type',
            field=models.CharField(max_length=100, verbose_name='Reactor Type'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='recipe_id',
            field=models.CharField(max_length=100, verbose_name='Recipe ID'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='recipe_last_change',
            field=models.DateTimeField(verbose_name='Last Change of Recipe'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='recipe_name',
            field=models.CharField(max_length=100, verbose_name='Recipe Name'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='recipe_version',
            field=models.CharField(max_length=100, verbose_name='Recipe Version'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='sap_material_no',
            field=models.CharField(max_length=100, verbose_name='SAP Material Number'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='sap_reactor_no',
            field=models.CharField(max_length=100, verbose_name='SAP Reactor Number'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='site',
            field=models.CharField(max_length=100, verbose_name='Site Name'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_end_additivation',
            field=models.DateTimeField(verbose_name='End Additivation Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_end_adjusting',
            field=models.DateTimeField(verbose_name='End Adjusting Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_end_cooling',
            field=models.DateTimeField(verbose_name='End Cooling Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_end_filling',
            field=models.DateTimeField(verbose_name='End Filling Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_end_filling_2',
            field=models.DateTimeField(verbose_name='End Second Filling Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_end_heating',
            field=models.DateTimeField(verbose_name='End Heating Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_end_reaction',
            field=models.DateTimeField(verbose_name='End Reaction Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_end_sampling',
            field=models.DateTimeField(verbose_name='End Sampling Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_recipe_end',
            field=models.DateTimeField(verbose_name='Recipe End Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_recipe_start',
            field=models.DateTimeField(verbose_name='Recipe Start Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_start_additivation',
            field=models.DateTimeField(verbose_name='Start Additivation Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_start_adjusting',
            field=models.DateTimeField(verbose_name='Start Adjusting Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_start_cooling',
            field=models.DateTimeField(verbose_name='Start Cooling Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_start_filling',
            field=models.DateTimeField(verbose_name='Start Filling Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_start_filling_2',
            field=models.DateTimeField(verbose_name='Start Second Filling Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_start_heating',
            field=models.DateTimeField(verbose_name='Start Heating Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_start_reaction',
            field=models.DateTimeField(verbose_name='Start Reaction Time'),
        ),
        migrations.AlterField(
            model_name='generaldata',
            name='timestamp_start_sampling',
            field=models.DateTimeField(verbose_name='Start Sampling Time'),
        ),
        migrations.AlterField(
            model_name='processdata',
            name='batch_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='process_data', to='processV.generaldata', verbose_name='Batch Number'),
        ),
        migrations.AlterField(
            model_name='processdata',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_entries', to='processV.processdataheader', verbose_name='Header'),
        ),
        migrations.AlterField(
            model_name='processdata',
            name='timestamp',
            field=models.DateTimeField(verbose_name='Timestamp'),
        ),
        migrations.AlterField(
            model_name='processdata',
            name='value',
            field=models.FloatField(default=0.0, verbose_name='Value'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='format',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Format'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='max_value_pcs',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(10000)], verbose_name='Maximum Value PCS'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='medium',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Medium'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='min_value_pcs',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Minimum Value PCS'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Header Name'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='tag_no',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tag Number'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='type_group',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Type Group'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='processdataheader',
            name='value_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Value Type'),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(upload_to='uploads/', verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Uploaded At'),
        ),
    ]
