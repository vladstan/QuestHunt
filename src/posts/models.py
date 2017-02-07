from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):

	CATEGORY_CHOICES = (
        ("ADV", "Adventure Travel"),
        ("ART", "Art & Culture"),
        ("BCK", "Backpacking"),
        ("FAM", "Family Holydays"),
        ("FOD", "Food & Drink"),
        ("ROD", "Road Trips"),
        ("BGT", "On a budget"),
        ("WIL", "Wildlife & Nature"),
    )


	title = models.CharField(max_length=140)
	slug = models.SlugField(unique = True)
	author = models.ForeignKey(User)
	category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default = 'ADV')
	description = models.TextField(default="Description")
	country = models.CharField(max_length=20, default = 'United States')
	region = models.CharField(max_length=20, default = 'Florida')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	photo = models.FileField(upload_to = 'posts', default='/media/posts/iceland.jpg')
	status = models.BooleanField(default = True)
	approved = models.BooleanField(default = True)
	featured = models.BooleanField(default = False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("post_details", kwargs = {'slug': self.slug})


def create_slug(instance, new_slug = None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug = slug).order_by('-id')
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug = new_slug)
	return slug

def pre_save_group_receiver(sender, instance, *args, **kwargds):
	if not instance .slug:
		instance.slug = create_slug(instance)


pre_save.connect(pre_save_group_receiver, sender = Post)