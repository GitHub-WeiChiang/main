# Generated by Django 3.1.2 on 2020-12-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpsDatingApp', '0010_auto_20201223_0148'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='profilePicture',
            new_name='profilePhoto',
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='sex',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='basicinfo',
            name='sexori',
            field=models.IntegerField(),
        ),
    ]
