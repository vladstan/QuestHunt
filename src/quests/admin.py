from django.contrib import admin

# Register your models here.

from .models import Quest, Tribe, Location

class QuestAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	search_fields = ["title", "description"]
	filter_horizontal = ('locations',)
	class Meta: 
		model = Quest

admin.site.register(Quest, QuestAdmin)
admin.site.register(Tribe)
admin.site.register(Location)