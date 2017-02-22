from django.shortcuts import render
from quests.models import Quest, Tribe

# Create your views here.

def home(request):
	quests = Quest.objects.filter(featured = True)
	tribes = Tribe.objects.all()
	context={
		"quests": quests,
		"tribes": tribes
	}
	return render(request, 'home.html', context)