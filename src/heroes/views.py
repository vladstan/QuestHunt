from django.shortcuts import render, get_object_or_404
from .models import Hero



# Create your views here.


def heroes(request):
	template = "heroes.html"
	context = {
		"title": "Heroes"
	}
	return render(request, template, context)

def hero_profile(request, slug = None):
	template = "hero_profile.html"
	hero = get_object_or_404(Hero, slug=slug)# we need to FIX this. Select only the tips for that destination
	context={
		"hero": hero
	}
	return render(request, template, context)
