from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from destinations.models import Destination
from tribes.models import Tribe

# Create your models here.


class LevelDestination(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	icon = models.FileField(upload_to = 'icons', default='/media/posts/iceland.jpg')
	points = models.IntegerField()

class HeroDestination(models.Model):
	user = models.ForeignKey(User)
	destination = models.ForeignKey(Destination)
	tribe = models.ManyToManyField(Tribe)
	days_spent = models.IntegerField()
	no_of_visits = models.IntegerField()
	points = models.IntegerField()

	def __str__(self):
		return self.user.username

class HeroTip(models.Model):
	user = models.ForeignKey(User)
	my_destination = models.ForeignKey(HeroDestination)
	title = models.CharField(max_length=140)
	description = models.TextField(max_length=1000)
	photo = models.FileField(upload_to = 'posts', default='/media/posts/iceland.jpg')

	def __str__(self):
		return self.user.username


class Hero(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="hero")
	slug = models.SlugField(unique = True)
	avatar = models.CharField(max_length = 500)
	video = models.CharField(max_length = 500)
	about = models.CharField(max_length = 1000)
	subscribers = models.ManyToManyField(User, blank=True, related_name="hero_subscribers")

	def __str__(self):
		return self.user.username


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		new_profile = Hero.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)

