# Generated by Django 3.2.7 on 2021-10-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kicker_app', '0004_auto_20211015_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='winner2',
            field=models.CharField(default='Max Mustermann', max_length=200),
        ),
    ]
