# Generated by Django 5.0 on 2023-12-12 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
        ('modal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='model_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='modal.modal'),
        ),
        migrations.AlterField(
            model_name='control',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]