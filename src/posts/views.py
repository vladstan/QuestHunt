from django.shortcuts import render, redirect,  get_object_or_404


# Create your views here.

from .models import Post, Categ

def post_details(request, slug = None):
	template = "post_details.html"
	post = get_object_or_404(Post, slug=slug)
	all_locations = post.locations.all()
	cities = [loc for loc in all_locations if loc.type == "city"]
	countries = [loc for loc in all_locations if loc.type == "country"]
	regions = [loc for loc in all_locations if loc.type == "region"]
	context={
		"post": post,
		"cities": cities,
		"countries": countries,
		"regions": regions,
		"categories": post.categories.all()
	}
	return render(request, template, context)


def posts_list(request):
	posts = Post.objects.filter(status=True)
	context = {
		"posts": posts
	}
	return render(request, 'posts_list.html', context)

def category(request, link):

	try:
		#we need to fox this.
		posts = Post.objects.filter(categories__slug__in = [link])
		current_categ = Categ.objects.get(slug = link)
		categs = Categ.objects.all()
		context = {
			"posts": posts,
			"categs": categs,
			"current_categ": current_categ,
		}
		return render(request, 'posts_list.html', context)

	except KeyError:
		return redirect('posts_list')	