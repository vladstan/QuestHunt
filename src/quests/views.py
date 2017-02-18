from django.shortcuts import render, redirect,  get_object_or_404


# Create your views here.

from .models import Quest, Categ

def quest_details(request, slug = None, link = None):
	template = "quest_details.html"
	quest = get_object_or_404(Quest, slug=slug)
	all_locations = quest.locations.all()
	cities = [loc for loc in all_locations if loc.type == "city"]
	countries = [loc for loc in all_locations if loc.type == "country"]
	regions = [loc for loc in all_locations if loc.type == "region"]
	context={
		"quest": quest,
		"cities": cities,
		"countries": countries,
		"regions": regions,
		"categories": quest.categories.all()
	}
	return render(request, template, context)


def quests_list(request):
	quests = Quest.objects.filter(status=True)
	context = {
		"quests": quests
	}
	return render(request, 'quests_list.html', context)

def category(request, link):

	try:
		#we need to fox this.
		quests = Quest.objects.filter(categories__slug__in = [link])
		current_categ = Categ.objects.get(slug = link)
		categs = Categ.objects.all()
		context = {
			"quests": quests,
			"categs": categs,
			"current_categ": current_categ,
		}
		return render(request, 'quests_list.html', context)

	except KeyError:
		return redirect('quests_list')	