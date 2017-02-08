from django.shortcuts import render, get_object_or_404

from .models import Profile
from posts.models import Post

# Create your views here.



def expert_profile(request, slug = None):
	template = "expert_profile.html"
	profile = get_object_or_404(Profile, slug=slug)
	posts = Post.objects.filter(status=True)
	context={
		"profile": profile,
		"posts": posts
	}
	return render(request, template, context)
