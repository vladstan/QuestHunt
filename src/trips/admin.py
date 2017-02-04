from django.contrib import admin

# Register your models here.

from .models import Trip

class TripAdmin(admin.ModelAdmin):
	list_display = ["__str__", "description", "price_quick_help", "price_full_trip" ]
	search_fields = ["title", "description"]
	list_filter = ["price_quick_help"]
	class Meta: 
		model = Trip


admin.site.register(Trip, TripAdmin)