# Generated by Django 5.0.2 on 2024-02-25 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver_app', '0002_cab_type_alter_cab_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cab',
            name='driver_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='driver_app.driver'),
        ),
    ]