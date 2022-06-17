# Generated by Django 3.1.2 on 2020-12-28 12:34

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0033_auto_20201228_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountstatus',
            name='enableFunction',
            field=django_mysql.models.ListCharField(models.IntegerField(), default=[], max_length=17, size=None),
        ),
        migrations.AlterField(
            model_name='accountstatus',
            name='lastRefreshTime',
            field=models.DateTimeField(default='1970-01-01 00:00:00.000000'),
        ),
        migrations.AlterField(
            model_name='matchinginfo',
            name='matchingAge',
            field=django_mysql.models.ListCharField(models.IntegerField(), default=[], max_length=5, size=None),
        ),
        migrations.AlterField(
            model_name='matchinginfo',
            name='matchingkind',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='pairingrecord',
            name='locate',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='registerinfo',
            name='registerLocate',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserveLocate',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='blockade',
            field=django_mysql.models.ListTextField(models.CharField(max_length=32), default=[], size=None),
        ),
        migrations.AlterField(
            model_name='socialinfo',
            name='friend',
            field=django_mysql.models.ListTextField(models.CharField(max_length=32), default=[], size=None),
        ),
    ]