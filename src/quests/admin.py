from django.contrib import admin

# Register your models here.

from .models import Quest, Categ, Location

class QuestAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	search_fields = ["title", "description"]
	filter_horizontal = ('locations',)
	class Meta: 
		model = Quest

admin.site.register(Quest, QuestAdmin)
admin.site.register(Categ)
admin.site.register(Location)