# Generated by Django 4.2.1 on 2024-01-26 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0033_rename_dataname_datarepository_data_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NationalStrategies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Directives', 'Directives'), ('Proclamations', 'Proclamations'), ('Regulations', 'Regulations'), ('Manual', 'Manual')], default='', max_length=100, null=True)),
                ('file', models.FileField(blank=True, max_length=500, null=True, upload_to='regulatory_framework/')),
                ('DataRepository', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regulatory_overview.datarepository')),
            ],
        ),
    ]
