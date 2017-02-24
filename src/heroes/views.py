from django.shortcuts import render, get_object_or_404
from .models import Hero, HeroDestination, HeroTip



# Create your views here.


def heroes(request):
	template = "heroes.html"
	context = {
		"title": "Heroes"
	}
	return render(request, template, context)

def hero_profile(request, slug = None):
	template = "hero_profile.html"
	hero = get_object_or_404(Hero, slug=slug)
	trips = HeroDestination.objects.filter(user = hero.user)
	tips = HeroDestination.objects.prefetch_related('herotip_set').all() # we need to FIX this. Select only the tips for that destination
	context={
		"hero": hero,
		"trips": trips,
		"tips": tips
	}
	return render(request, template, context)

def trip_details(request, slug, link):
	template = "trip_details.html"
	hero = get_object_or_404(Hero, slug=slug)
	trip = get_object_or_404(HeroDestination, id=1)
	tips = HeroDestination.objects.prefetch_related('herotip_set').all()
	context = {
		"hero": hero,
		"trip": trip,
		"tips": tips
	}
	return render(request, template, context)