# Generated by Django 3.1.2 on 2021-04-03 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0065_auto_20210328_0054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pairingrecord',
            old_name='locate',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='registerinfo',
            old_name='registerLocate',
            new_name='registerCity',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='reserveLocate',
            new_name='reserveCity',
        ),
    ]
