from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from profile.models import Profile
from tribes.models import Tribe
from destinations.models import Destination

# Create your models here.



class Quest(models.Model):


	title = models.CharField(max_length=140)
	slug = models.SlugField(unique = True)
	author = models.ForeignKey(Profile)
	summary = models.TextField(default="Summary Here")
	tribes = models.ManyToManyField(Tribe)
	content = models.TextField(default="content")
	gmaps_embed_url = models.TextField(blank=True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	cover_image = models.FileField(upload_to = 'posts', default='/media/posts/iceland.jpg')
	#add photo section
	status = models.BooleanField(default = True)
	approved = models.BooleanField(default = True)
	featured = models.BooleanField(default = False)
	destinations = models.ManyToManyField(Destination)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("quest_details", kwargs = {'slug': self.slug})

def create_slug(instance, new_slug = None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Quest.objects.filter(slug = slug).order_by('-id')
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug = new_slug)
	return slug

def pre_save_group_receiver(sender, instance, *args, **kwargds):
	if not instance .slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_group_receiver, sender = Quest)



