# Generated by Django 4.2.1 on 2023-08-04 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0014_alter_paid_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paid',
        ),
    ]
