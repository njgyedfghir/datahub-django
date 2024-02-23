# Generated by Django 3.1.7 on 2022-08-12 22:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('indicator', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('indicator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.indicator')),
            ],
        ),
    ]
