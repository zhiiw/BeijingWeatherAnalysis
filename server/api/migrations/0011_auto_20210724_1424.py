# Generated by Django 3.2.5 on 2021-07-24 06:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210724_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beijing',
            fields=[
                ('date', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('tmax', models.IntegerField(blank=True, null=True)),
                ('tmin', models.IntegerField(blank=True, null=True)),
                ('tavg', models.IntegerField(blank=True, null=True)),
                ('prcp', models.FloatField(blank=True, null=True)),
                ('con', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'Beijing',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(default=datetime.datetime(2021, 7, 24, 6, 23, 58, 143722, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='time_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 24, 6, 23, 58, 143722, tzinfo=utc)),
        ),
    ]
