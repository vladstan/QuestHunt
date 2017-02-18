from django.shortcuts import render
from quests.models import Quest, Categ

# Create your views here.

def home(request):
	quests = Quest.objects.filter(featured = True)
	categs = Categ.objects.all()
	context={
		"quests": quests,
		"categs": categs
	}
	return render(request, 'home.html', context)