# Generated by Django 4.2.1 on 2023-08-05 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0017_post_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='SubCategory',
            new_name='subcategory',
        ),
    ]
