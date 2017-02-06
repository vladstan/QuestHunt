from django.shortcuts import render
from trips.models import Trip

# Create your views here.

def home(request):
	trips = Trip.objects.filter(featured = True)
	return render(request, 'home.html', {'trips': trips})