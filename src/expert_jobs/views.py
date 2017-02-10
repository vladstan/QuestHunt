from django.shortcuts import render


# Create your views here.


def landing(request):
	template = "landing_experts.html"
	context={
		"title": "Here is the title",
	}
	return render(request, template, context)
