# Generated by Django 5.0.7 on 2024-07-12 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parcel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='update_date_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
