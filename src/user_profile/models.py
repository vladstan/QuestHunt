from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	avatar = models.CharField(max_length = 500)
	email = models.CharField(max_length = 500, default = 'me@email.com')
	about = models.CharField(max_length = 1000)
	followers = models.CharField(max_length = 500)
	price_quick_help = MoneyField(
		decimal_places=2,
        default=29,
        default_currency='USD',
        max_digits=11,
    )
	price_full_help = MoneyField(
		decimal_places=2,
        default=99,
        default_currency='USD',
        max_digits=11,
    )

	def __str__(self):
		return self.user.username