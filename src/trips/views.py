from django.shortcuts import render, redirect,  get_object_or_404

# Create your views here.

from .models import Trip

def trip_details(request, slug = None):
	template = "trip_details.html"
	trip = get_object_or_404(Trip, slug=slug)
	context={
		"trip": trip
	}
	return render(request, template, context)


def trips_list(request):
	trips = Trip.objects.filter(status=True)
	return render(request, 'trips_list.html', {"trips": trips})

def category(request, link):
	categories = {
		"adventure" : "ADV",
		"art-culture" : "ART",
		"backpacking" : "BKP",
		"family-holidays" : "FAM",
		"food-drink" : "FOD",
		"road-trips" : 'ROD',
		"budget" : 'BGT',
		"wildlife-nature": 'WIL'
	}

	try:
		trips = Trip.objects.filter(category = categories[link])
		return render(request, 'trips_list.html', {'trips': trips})

	except KeyError:
		return redirect('trips_list')	