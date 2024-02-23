# Generated by Django 4.2.1 on 2024-01-24 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0031_datarepository_importantlinks_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datarepository',
            name='Data_Name',
        ),
        migrations.AddField(
            model_name='datarepository',
            name='DataName',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]