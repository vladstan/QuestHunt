from django.shortcuts import render
from posts.models import Post, Categ

# Create your views here.

def home(request):
	posts = Post.objects.filter(featured = True)
	categs = Categ.objects.all()
	context={
		"posts": posts,
		"categs": categs
	}
	return render(request, 'home.html', context)