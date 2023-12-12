# Generated by Django 5.0 on 2023-12-12 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input', '0003_alter_input_model_id_alter_input_name'),
        ('modal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='model_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modal.modal'),
        ),
        migrations.AlterField(
            model_name='input',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]