# Generated by Django 2.0.5 on 2018-06-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api', '0010_auto_20180524_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=100)),
                ('certificate', models.CharField(max_length=250)),
            ],
        ),
    ]
