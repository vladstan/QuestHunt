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
