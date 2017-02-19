from django.shortcuts import render

# Create your views here.


def pricing(request):
	template = "pricing.html"
	context={}
	return render(request, template, context)
