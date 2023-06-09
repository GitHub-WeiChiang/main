# Generated by Django 3.1.2 on 2021-01-22 16:50

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0053_auto_20210123_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='lifeSharingOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.UUIDField()),
                ('order', django_mysql.models.ListCharField(models.IntegerField(), default=[0, 1, 2, 3, 4, 5], max_length=11, size=None)),
            ],
        ),
    ]
