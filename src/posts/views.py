from django.shortcuts import render, redirect,  get_object_or_404

# Create your views here.

from .models import Post

def post_details(request, slug = None):
	template = "post_details.html"
	post = get_object_or_404(Post, slug=slug)
	context={
		"post": post
	}
	return render(request, template, context)


def posts_list(request):
	posts = Post.objects.filter(status=True)
	return render(request, 'posts_list.html', {"posts": posts})

def category(request):

	print = request

	try:
		posts = Post.objects.filter(category = request)
		return render(request, 'posts_list.html', {'posts': posts})

	except KeyError:
		return redirect('posts_list')	