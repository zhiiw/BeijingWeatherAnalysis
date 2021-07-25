
from django.db import models

from django.utils import timezone


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=30)
    time_created = models.DateTimeField(default=timezone.now())
    password = models.TextField()
    last_login = models.DateField(default=timezone.now())

    def __str__(self):
        return self.username


class Rank5(models.Model):
    name = models.CharField(primary_key=True, max_length=128, db_collation='utf8_bin')
    score = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'rank5'


class Prewholeyear(models.Model):
    date = models.CharField(primary_key=True, max_length=45, null=False)
    tmax = models.FloatField(blank=True, null=True)
    tavg = models.FloatField(blank=True, null=True)
    tmin = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'preWholeYear'


class Beijing(models.Model):
    date = models.CharField(primary_key=True, max_length=45)
    tmax = models.IntegerField(blank=True, null=True)
    tmin = models.IntegerField(blank=True, null=True)
    tavg = models.IntegerField(blank=True, null=True)
    prcp = models.FloatField(blank=True, null=True)
    con = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Beijing'




