# Generated by Django 4.2.1 on 2023-08-05 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0016_category_subcategory_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='SubCategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='regulatory_overview.subcategory'),
        ),
    ]