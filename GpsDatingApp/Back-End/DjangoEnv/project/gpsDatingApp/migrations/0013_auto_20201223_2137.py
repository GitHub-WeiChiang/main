# Generated by Django 3.1.2 on 2020-12-23 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0012_auto_20201223_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accountstatus',
            old_name='lastLoginTime',
            new_name='lastRefreshTime',
        ),
    ]
