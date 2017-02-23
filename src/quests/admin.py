from django.contrib import admin

# Register your models here.

from .models import Quest

class QuestAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	search_fields = ["title", "description"]
	filter_horizontal = ('destinations',)
	class Meta: 
		model = Quest

admin.site.register(Quest, QuestAdmin)

