# Generated by Django 5.0.1 on 2024-01-31 08:58

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_regulatoryoverview_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='iso_code',
        ),
        migrations.RemoveField(
            model_name='country',
            name='name',
        ),
        migrations.RemoveField(
            model_name='regulatoryoverview',
            name='country',
        ),
        migrations.AddField(
            model_name='country',
            name='country',
            field=django_countries.fields.CountryField(default='US', max_length=2),
        ),
        migrations.AddField(
            model_name='regulatoryoverview',
            name='Region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.country'),
        ),
    ]
