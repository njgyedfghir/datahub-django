# Generated by Django 5.0.1 on 2024-02-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0046_alter_region_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='nationalstrategies',
            name='pdfTitle',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
