# Generated by Django 3.1.2 on 2020-12-28 07:45

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0016_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicinfo',
            name='interest',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=30, size=5),
        ),
    ]
