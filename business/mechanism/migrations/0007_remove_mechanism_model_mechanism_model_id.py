# Generated by Django 5.0 on 2023-12-12 19:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechanism', '0006_remove_mechanism_model_id_mechanism_model'),
        ('modal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mechanism',
            name='model',
        ),
        migrations.AddField(
            model_name='mechanism',
            name='model_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modal.modal'),
        ),
    ]