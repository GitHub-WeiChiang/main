# Generated by Django 3.1.2 on 2021-01-08 16:44

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0050_auto_20210109_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialinfo',
            name='blockade',
            field=django_mysql.models.ListTextField(models.CharField(max_length=36), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='friend',
            field=django_mysql.models.ListTextField(models.CharField(max_length=36), default=[], size=None),
        ),
    ]
