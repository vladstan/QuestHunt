from django.shortcuts import render

# Create your views here.

def home(request):
	groups = ['Group1', 'Grouop2']
	return render(request, 'home.html', {'groups': groups})