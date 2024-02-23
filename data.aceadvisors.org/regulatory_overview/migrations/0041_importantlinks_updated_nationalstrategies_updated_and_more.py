# Generated by Django 5.0.1 on 2024-01-31 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0040_region_year_nationalstrategies_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='importantlinks',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='nationalstrategies',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='regulatoryframework',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]