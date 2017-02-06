from django.contrib import admin

# Register your models here.

from .models import Trip

class TripAdmin(admin.ModelAdmin):
	list_display = ["__str__", "country"]
	search_fields = ["title", "description"]
	list_filter = ["country", "region", "category"]
	class Meta: 
		model = Trip


admin.site.register(Trip, TripAdmin)