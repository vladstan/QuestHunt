from django.contrib import admin
from .models import Hero, HeroTrip, TripQuest

# Register your models here.


class HeroAdmin(admin.ModelAdmin):
	list_display = ["__str__",]
	class Meta: 
		model = Hero


class TripQuestInline(admin.TabularInline):
    model = TripQuest

class HeroTripAdmin(admin.ModelAdmin):
    inlines = (TripQuestInline,)

admin.site.register(Hero, HeroAdmin)
admin.site.register(HeroTrip, HeroTripAdmin)
