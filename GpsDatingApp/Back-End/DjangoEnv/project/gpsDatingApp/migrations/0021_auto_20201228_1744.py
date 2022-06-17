# Generated by Django 3.1.2 on 2020-12-28 09:44

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0020_remove_accountstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancedinfo',
            name='disposition',
            field=django_mysql.models.ListCharField(models.IntegerField(), default=[], max_length=30, size=5),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='interest',
            field=django_mysql.models.ListCharField(models.IntegerField(), default=[], max_length=30, size=5),
        ),
    ]