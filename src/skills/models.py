from django.db import models

# Create your models here.


class Skill(models.Model):
	name = 
	description = 
	slug = 
	icon = 
	

class TribePointsAward(models.Model):
	hero = models.ForeignKey(User)
	quest = 
	points  = 
	tribe =


class DestinationPointsAward(models.Model):
	hero = models.ForeignKey(User)
	quest = 
	points  = 
	tribe = 

