from django.shortcuts import render

# Create your views here.

def masters(request):

	context = {
		"title" : "Masters"
	}
	return render(request, 'masters.html', context)

