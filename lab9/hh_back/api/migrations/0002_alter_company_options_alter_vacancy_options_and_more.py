# Generated by Django 5.0.3 on 2024-04-11 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
    ]
