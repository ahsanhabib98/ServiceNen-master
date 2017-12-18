# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Division(models.Model):
    division_name = models.CharField(max_length=50)
    def __str__(self):
        return self.division_name

class District(models.Model):
    district_name = models.CharField(max_length=50)
    division = models.ForeignKey(Division)
    def __str__(self):
        return self.district_name

class Area(models.Model):
    area_name = models.CharField(max_length=50)
    District = models.ForeignKey(District)
    def __str__(self):
        return self.area_name

class Profile(models.Model):
    title_choice = (
        ('Mr.','Mr'),
        ('Miss','Miss'),
        ('Ms.','Ms.'),
        ('Mrs.','Mrs'),
        ('Ir.','Ir'),
        ('Dr.','Dr'),
        ('Drs','Drs'),
        ('Professor','Professor'),
    )
    gender_choice = (
        ('Male','Male'),
        ('Female','Female'),
    )
    shirt_choice = (
        ('XS','XS'),
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL'),
        ('XXXL','XXXL'),
        ('XXXXL','XXXXL'),
    )
    user = models.OneToOneField(User)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    profile_name = models.CharField(max_length=50)
    title = models.CharField(max_length=20, choices=title_choice)
    gender = models.CharField(max_length=10, choices=gender_choice)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shirt_size = models.CharField(max_length=10,choices=shirt_choice)
    area = models.ForeignKey(Area)
    occupation = models.CharField(max_length=20)
    Institution = models.CharField(max_length=20)
    # birth_day = models.DateField()
    phone = models.IntegerField()
    qualification = models.TextField()
    def __str__(self):
        return self.profile_name

# Create your models here.
