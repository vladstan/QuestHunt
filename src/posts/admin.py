from django.contrib import admin

# Register your models here.

from .models import Post
from .models import Category


class PostAdmin(admin.ModelAdmin):
	list_display = ["__str__", "country"]
	search_fields = ["title", "description"]
	list_filter = ["country", "region", "category"]
	class Meta: 
		model = Post


admin.site.register(Post, PostAdmin)
admin.site.register(Category)