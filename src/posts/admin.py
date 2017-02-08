from django.contrib import admin

# Register your models here.

from .models import Post, Categ, Location


class PostAdmin(admin.ModelAdmin):
	list_display = ["__str__"]
	search_fields = ["title", "description"]
	class Meta: 
		model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Categ)
admin.site.register(Location)