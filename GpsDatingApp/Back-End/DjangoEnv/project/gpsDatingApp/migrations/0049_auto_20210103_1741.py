# Generated by Django 3.1.2 on 2021-01-03 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0048_auto_20210103_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='isRegister',
            field=models.BooleanField(default=False),
        ),
    ]
