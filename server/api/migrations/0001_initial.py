# Generated by Django 3.2.5 on 2021-07-22 08:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('permission', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=30)),
                ('num_followers', models.IntegerField(default=0)),
                ('num_following', models.IntegerField(default=0)),
                ('time_created', models.DateTimeField(default=datetime.datetime(2021, 7, 22, 8, 13, 8, 948125, tzinfo=utc))),
                ('password', models.TextField()),
                ('last_login', models.DateField(default=datetime.datetime(2021, 7, 22, 8, 13, 8, 948125, tzinfo=utc))),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
