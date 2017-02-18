from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	slug = models.SlugField(unique = True)
	avatar = models.CharField(max_length = 500)
	video = models.CharField(max_length = 500)
	email = models.CharField(max_length = 500, default = 'me@email.com')
	about = models.CharField(max_length = 1000)
	is_master = models.BooleanField(default=False)
	subscribers = models.CharField(max_length = 500)


	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return reverse("expert_profile", kwargs = {'slug': self.slug})

class Gig(models.Model):
	name = models.CharField(max_length=100, default="Quick Help")
	price = models.IntegerField(default=29)
	description = models.CharField(max_length=300, default="I am here to help you with")
	value_one = models.CharField(max_length=50, default="Save up to $300 on a trip")
	value_two = models.CharField(max_length=50, default="Make the most out of the trip")
	value_three = models.CharField(max_length=50, default="Connect with great locals")
	profile = models.ForeignKey(Profile)


	def __str__(self):
		return self.name

class Review(models.Model):
	author = models.ForeignKey(User)
	rating = models.IntegerField()
	body = models.CharField(max_length=1000, blank=True)
	profile = models.ForeignKey(Profile)


	def __str__(self):
		return self.author