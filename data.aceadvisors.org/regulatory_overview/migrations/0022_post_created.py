# Generated by Django 4.2.1 on 2023-08-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0021_post_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
