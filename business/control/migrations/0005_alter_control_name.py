# Generated by Django 5.0 on 2023-12-12 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_alter_control_model_id_alter_control_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
