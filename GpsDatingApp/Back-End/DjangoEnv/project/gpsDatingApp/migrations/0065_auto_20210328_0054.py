# Generated by Django 3.1.2 on 2021-03-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0064_auto_20210328_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='pairingrecord',
            name='district',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pairingrecord',
            name='locate',
            field=models.CharField(default='', max_length=50),
        ),
    ]