# Generated by Django 2.0.5 on 2018-05-24 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api', '0009_education_minor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='certificate',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='minor',
            field=models.CharField(blank=True, default=None, max_length=250),
        ),
    ]