# Generated by Django 2.0.5 on 2018-05-24 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api', '0005_auto_20180524_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skilltype',
            name='image',
        ),
        migrations.RemoveField(
            model_name='skilltype',
            name='proficieny',
        ),
        migrations.AlterField(
            model_name='skillset',
            name='skill',
            field=models.CharField(max_length=50),
        ),
    ]
