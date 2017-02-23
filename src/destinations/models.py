from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Destination(models.Model):
	type = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	slug = models.SlugField(unique = True)
	cover_image = models.FileField(upload_to = 'posts', default='/media/posts/iceland.jpg')
	description = models.TextField(max_length=1000, default="Get notified every time we publish a new tip, a new hack or a deal on Adventure Travel.")
	subscribers = models.ManyToManyField(User, blank=True)

	def __str__(self):
		return self.name

	def get_destination_subscribers(self):
		return self.subscribers.all()