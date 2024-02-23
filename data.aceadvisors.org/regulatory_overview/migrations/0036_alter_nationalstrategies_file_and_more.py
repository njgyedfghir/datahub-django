# Generated by Django 5.0.1 on 2024-01-29 21:41

import regulatory_overview.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0035_nationalstrategies_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nationalstrategies',
            name='file',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to=regulatory_overview.models.pdf_file_upload_to),
        ),
        migrations.AlterField(
            model_name='regulatoryframework',
            name='file',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to=regulatory_overview.models.pdf_file_upload_to),
        ),
    ]
