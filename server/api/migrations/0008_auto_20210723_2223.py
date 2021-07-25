# Generated by Django 3.2.5 on 2021-07-23 14:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210723_1531'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prewholeyear',
            options={'managed': True},
        ),
        migrations.RemoveField(
            model_name='user',
            name='photo_url',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2021, 7, 23, 14, 23, 51, 369592, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 23, 14, 23, 51, 368594, tzinfo=utc)),
        ),
    ]