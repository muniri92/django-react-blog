# Generated by Django 2.0.5 on 2018-06-10 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api', '0012_auto_20180610_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='end_date',
            field=models.DateField(verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='start_date',
            field=models.DateField(verbose_name='Start Date'),
        ),
    ]
