# Generated by Django 3.1.2 on 2020-12-13 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0002_delete_verifyinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reserveCoordinate',
        ),
    ]