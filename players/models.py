# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Player(models.Model):
	year = models.CharField(max_length=50)
	height = models.IntegerField()
	hometown = models.CharField(max_length=50)
	name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	weight = models.IntegerField()
	conference = models.CharField(max_length=50)
	team = models.CharField(max_length=50)
	division = models.CharField(max_length=50)
