# Generated by Django 4.0.3 on 2022-04-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_rename_date_measurement_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name': 'Датчик', 'verbose_name_plural': 'Датчики'},
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_name',
            field=models.CharField(max_length=30, verbose_name='Название'),
        ),
    ]
