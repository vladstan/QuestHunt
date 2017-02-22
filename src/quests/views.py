from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect,  get_object_or_404
from django.views import View

# Create your views here.

from .models import Quest, Tribe

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
		"tribes": quest.tribes.all()
	}
	return render(request, template, context)


def quests_list(request):
	quests = Quest.objects.filter(status=True)
	context = {
		"quests": quests
	}
	return render(request, 'quests_list.html', context)

def tribe(request, link):

	try:
		#we need to fox this.
		quests = Quest.objects.filter(tribes__slug__in = [link])
		current_tribe = Tribe.objects.get(slug = link)
		tribes = Tribe.objects.all()
		context = {
			"quests": quests,
			"tribes": tribes,
			"current_tribe": current_tribe,
		}
		return render(request, 'quests_list.html', context)

	except KeyError:
		return redirect('quests_list')	

class UserSubcribeTribeView(View):
	def get(self, request, link, *args, **kwargs):
		toggle_tribe = get_object_or_404(Tribe, slug = link)
		print(toggle_tribe.slug)
		print(toggle_tribe.members.all().count())
		if request.user.is_authenticated():
			if request.user in toggle_tribe.members.all():
				toggle_tribe.members.remove(request.user)
			else:
				toggle_tribe.members.add(request.user)
		return redirect("tribe", link=toggle_tribe.slug)


