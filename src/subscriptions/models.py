from django.db import models

# Create your models here.


class ExpertSubscription(models.Model):
	email = models.CharField(max_length=100, default="me@me.com")

	def __str__(self):
		return self.email


class CategorySubscription(models.Model):
	email = models.CharField(max_length=100, default="me@me.com")

	def __str__(self):
		return self.email


class DestinationSubscription(models.Model):
	email = models.CharField(max_length=100, default="me@me.com")

	def __str__(self):
		return self.email