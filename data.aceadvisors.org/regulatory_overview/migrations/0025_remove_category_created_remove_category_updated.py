# Generated by Django 4.2.1 on 2023-08-08 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0024_category_created_category_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created',
        ),
        migrations.RemoveField(
            model_name='category',
            name='updated',
        ),
    ]