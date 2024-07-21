# Generated by Django 5.0.7 on 2024-07-11 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostMachin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=False)),
                ('post_machin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_machin.postmachin')),
            ],
        ),
    ]
