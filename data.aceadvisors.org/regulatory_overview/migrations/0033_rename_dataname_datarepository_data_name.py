# Generated by Django 4.2.1 on 2024-01-24 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0032_remove_datarepository_data_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datarepository',
            old_name='DataName',
            new_name='Data_Name',
        ),
    ]