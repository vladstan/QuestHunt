from django.contrib import admin

from .models import Profile, Gig, Review

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
	list_display = ["__str__", "email"]
	search_fields = ["title", "description"]
	list_filter = ["is_expert", "gig"]
	class Meta: 
		model = Profile

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Gig)
admin.site.register(Review)
