# Generated by Django 5.0.1 on 2024-01-31 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regulatory_overview', '0041_importantlinks_updated_nationalstrategies_updated_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='importantlinks',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='nationalstrategies',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='regulatoryframework',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]