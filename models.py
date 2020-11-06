from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.db import models
from math import *
from decimal import *
from django.db import models


import json


# Create your models here.

class AllData(models.Model):
    exercise_id = models.BigIntegerField(db_column='Exercise_id', primary_key=True)  # Field name made lowercase.
    no_sessions_field = models.BigIntegerField(db_column='No.sessions ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    day_field = models.CharField(db_column='Day ', max_length= 30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    week = models.BigIntegerField(db_column='Week', blank=True, null=True)  # Field name made lowercase.
    month = models.CharField(db_column='Month', max_length= 30, blank=True, null=True)  # Field name made lowercase.
    exercise = models.CharField(db_column='Exercise', max_length= 30, blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(db_column='Longitude', max_length= 30, blank=True, null=True)  # Field name made lowercase.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'all_data'




class Venue(models.Model):

    name = models.CharField(max_length=255)

    latitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

    longitude = models.DecimalField(
                max_digits=9, decimal_places=6, null=True, blank=True)

class SalesRecord(models.Model):
	Region = models.CharField(max_length=100)
	Country = models.CharField(max_length=50)
	City = models.CharField(max_length=50)
	TotalSales = models.IntegerField()

	def __unicode__(self):
		return u'%s %s %s %s' % (self.Region, self.Country, self.City, self.TotalSales)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_researcher = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_physician= models.BooleanField(default=False)

class researcher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
class patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
class physician(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Exercise(models.Model):
    name = models.CharField(max_length=30)
    #color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name



class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Data(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='data')
    name = models.CharField(max_length=255)
    exercise = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Play(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

class TakenExercise(models.Model):
    #student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_exercise')
    quiz = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='taken_exercise')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
