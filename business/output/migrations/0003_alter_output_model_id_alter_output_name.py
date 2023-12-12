# Generated by Django 5.0 on 2023-12-12 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modal', '0001_initial'),
        ('output', '0002_alter_output_model_id_alter_output_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='model_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modal.modal'),
        ),
        migrations.AlterField(
            model_name='output',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]