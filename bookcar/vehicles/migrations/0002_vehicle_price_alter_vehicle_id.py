# Generated by Django 5.0.2 on 2024-02-17 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='price',
            field=models.IntegerField(default=41000),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]