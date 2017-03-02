from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class Master(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE, related_name="master")
	slug = models.SlugField(unique = True)
	avatar = models.CharField(max_length = 500)
	video = models.CharField(max_length = 500)
	about = models.CharField(max_length = 1000)
	subscribers = models.ManyToManyField(User, blank=True, related_name="master_subscribers")

	def __str__(self):
		return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
	if created:
		new_profile = Hero.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)