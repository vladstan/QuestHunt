from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from destinations.models import Destination
from quests.models import Quest

# Create your models here.



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


class HeroTrip(models.Model):
	name = models.CharField(blank=False, default="Name your trip", max_length=500)
	quests = models.ManyToManyField(Quest, through='TripQuest')

	def __str__(self):
		return self.name


class TripQuest(models.Model):
	quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
	hero_trip = models.ForeignKey(HeroTrip, on_delete=models.CASCADE)
	date_accepted = models.DateField()
	status = models.BooleanField(default=False)



