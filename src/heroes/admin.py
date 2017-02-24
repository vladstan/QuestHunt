from django.contrib import admin
from .models import Hero, HeroDestination, HeroTip

# Register your models here.


class HeroAdmin(admin.ModelAdmin):
	list_display = ["__str__",]
	class Meta: 
		model = Hero

admin.site.register(Hero, HeroAdmin)
admin.site.register(HeroDestination)
admin.site.register(HeroTip)