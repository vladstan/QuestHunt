from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect,  get_object_or_404


# Create your views here.


from .models import Quest
from tribes.models import Tribe
from destinations.models import Destination

def quests(request):
	quests = Quest.objects.all()
	context = {
		"quests": quests,
	}
	return render(request, "quests.html", context)

def quest_details(request, slug = None, link = None):
	template = "quest_details.html"
	quest = get_object_or_404(Quest, slug=slug)
	all_locations = quest.destinations.all()
	cities = [loc for loc in all_locations if loc.type == "city"]
	countries = [loc for loc in all_locations if loc.type == "country"]
	regions = [loc for loc in all_locations if loc.type == "region"]
	context={
		"quest": quest,
		"cities": cities,
		"countries": countries,
		"regions": regions,
		"tribes": quest.tribes.all()
	}
	return render(request, template, context)






