# Generated by Django 4.1 on 2022-09-04 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_alter_indicator_banner_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='acedata',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]