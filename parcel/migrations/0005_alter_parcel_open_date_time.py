# Generated by Django 5.0.7 on 2024-07-18 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0004_parcel_locker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parcel',
            name='open_date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]