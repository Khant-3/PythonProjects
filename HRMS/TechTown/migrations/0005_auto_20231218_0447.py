# Generated by Django 2.2 on 2023-12-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TechTown', '0004_auto_20231218_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeeattendance',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]