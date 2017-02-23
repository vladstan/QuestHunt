from django.shortcuts import render
from .models import Destination

from tribes.models import Tribe
from quests.models import Quest

# Create your views here.


def destinations(request):
	try: 
		destinations = Destination.objects.all()
		context = {
			"destinations": destinations
		}
		return render(request, 'destinations.html', context)
	except KeyError:
		return redirect('quest_list')

def destination(request, link):

	try:
		#we need to fox this.
		current_destination = Destination.objects.get(slug = link)
		tribes = Tribe.objects.all()
		print(link)
		quests = Quest.objects.filter(destinations__slug__in = [link])
		context = {
			"tribes": tribes,
			"current_destination": current_destination,
			"quests": quests,
		}
		return render(request, 'destination.html', context)

	except KeyError:
		return redirect('tribes')	