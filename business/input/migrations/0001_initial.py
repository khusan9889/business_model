# Generated by Django 5.0 on 2023-12-12 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modal.modal')),
            ],
        ),
    ]