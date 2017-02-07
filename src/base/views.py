from django.shortcuts import render
from posts.models import Post

# Create your views here.

def home(request):
	posts = Post.objects.filter(featured = True)
	return render(request, 'home.html', {'posts': posts})