
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


class Try(models.Model):
    date = models.CharField(primary_key=True, max_length=45)
    tmax = models.IntegerField(blank=True, null=True)
    tavg = models.IntegerField(blank=True, null=True)
    tmin = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    con = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'try'


class Comments(models.Model):
    id = models.BigAutoField(primary_key=True)
    createTime = models.DateTimeField(default=timezone.now())
    text = models.TextField(max_length=60)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )


class Temperatures(models.Model):
    index = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=45, blank=True, null=True)
    date = models.CharField(max_length=45, blank=True, null=True)
    tmax = models.IntegerField(blank=True, null=True)
    tmin = models.IntegerField(blank=True, null=True)
    tavg = models.IntegerField(blank=True, null=True)
    prcp = models.FloatField(blank=True, null=True)
    con = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'temperatures'






