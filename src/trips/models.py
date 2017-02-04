from django.db import models

from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify

# Create your models here.

class Trip(models.Model):
	title = models.CharField(max_length=140)
	slug = models.SlugField(unique = True)
	description = models.TextField(default="Description")
	price_quick_help = models.DecimalField(max_digits=3, decimal_places=2, default=20)
	price_full_trip = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("trip_details", kwargs = {'slug': self.slug})


def create_slug(instance, new_slug = None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Trip.objects.filter(slug = slug).order_by('-id')
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug = new_slug)
	return slug

def pre_save_group_receiver(sender, instance, *args, **kwargds):
	if not instance .slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_group_receiver, sender = Trip)