from django.shortcuts import render, get_object_or_404

from .models import Profile, Gig
from quests.models import Quest

# Create your views here.



def master_profile(request, slug = None):
	template = "master_profile.html"
	profile = get_object_or_404(Profile, slug=slug)
	quests = Quest.objects.filter(status=True, author=profile)
	context={
		"profile": profile,
		"quests": quests
	}
	return render(request, template, context)
