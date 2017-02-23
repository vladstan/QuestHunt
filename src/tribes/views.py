from django.shortcuts import render, redirect,  get_object_or_404
from django.views import View

# Create your views here.

from quests.models import Quest
from tribes.models import Tribe


def tribes(request):
 	tribes = Tribe.objects.all()
 	context = {
 		"tribes": tribes
 	}
 	return render(request, 'tribes.html', context)

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
		return render(request, 'tribe.html', context)

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

